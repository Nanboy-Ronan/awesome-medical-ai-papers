"""Transparent screening, README reconciliation, and auditable local reports."""

from __future__ import annotations

from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from difflib import SequenceMatcher
import csv
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlparse

from .sources import Client, Paper, clean, key, soup


def canonical_url(url: str) -> str:
    url = url.replace("http://", "https://").rstrip("/")
    url = url.replace("papers.nips.cc", "proceedings.neurips.cc").replace("papers.neurips.cc", "proceedings.neurips.cc")
    url = url.replace("www.openaccess.thecvf.com", "openaccess.thecvf.com")
    if re.match(r"https://(?:www\.)?arxiv.org/(?:abs|pdf)/", url):
        identifier = re.split(r"/(?:abs|pdf)/", url, maxsplit=1)[1].split("?")[0].split("#")[0]
        identifier = re.sub(r"v\d+$", "", identifier.removesuffix(".pdf"))
        return f"arxiv:{identifier}"
    url = re.sub(r"https://(?:www\.)?dl.acm.org/doi/(?:abs/|pdf/)?", "https://doi.org/", url)
    url = re.sub(r"openreview.net/(?:pdf|forum)\?id=", "openreview.net/forum?id=", url)
    match = re.search(r"https://(?:proceedings.neurips.cc|proceedings.iclr.cc)/paper_files/paper/(\d{4})/(?:file|hash)/([a-f\d]+)-", url)
    if match:
        return f"{urlparse(url).netloc}:{match[1]}:{match[2]}"
    if "openaccess.thecvf.com/content/" in url:
        url = url.replace("/papers/", "/html/").replace("_paper.pdf", "_paper.html")
    return url


def is_paper_url(url: str) -> bool:
    return bool(re.search(r"/(?:html/|hash/|file/|article/view/|forum\?id=|abs/|pdf/)|doi.org/10\.|/v\d+/[^/]+\.html|aclanthology.org/\d{4}\.[^/]+\.\d+", url))


def read_readme(path: Path) -> list[dict]:
    result = []
    venue = None
    year = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        heading = re.match(r"### (.+) (20\d{2})$", line)
        if heading:
            venue, year = heading[1], int(heading[2])
        match = re.match(r"- \*\*\[(.+?)\]\((https?://[^\s)]+)\)\*\*", line)
        if match:
            result.append({"title": match[1], "url": match[2], "venue": venue, "year": year, "line": number})
    return result


class Rules:
    def __init__(self, path: Path):
        content = path.read_bytes()
        self.data = json.loads(content)
        self.sha256 = hashlib.sha256(content).hexdigest()
        self.patterns = {topic: self.compile_terms(terms) for topic, terms in self.data["topics"].items()}
        self.extra_patterns = {name: self.compile_terms(self.data[name])
                               for name in ("broad_review", "pure_biology", "clinical_rescue")}
        self.guards = {name: re.compile(r"(?<!\w)(?:" + "|".join(
                           re.escape(term) + (r"(?!\w)" if len(term) <= 4 else "") for term, _ in patterns) + ")", re.I)
                       for name, patterns in {**self.patterns, **self.extra_patterns}.items()}

    @staticmethod
    def compile_terms(terms: list[str]) -> list[tuple[str, re.Pattern]]:
        # Bound short abbreviations to avoid e.g. CT inside "contrastive", EMR
        # inside unrelated words, or BCI inside a model name.
        return [(term, re.compile(r"(?<!\w)" + re.escape(term) + (r"(?!\w)" if len(term) <= 4 else ""), re.I)) for term in terms]

    @staticmethod
    def matches(patterns: list[tuple[str, re.Pattern]], text: str) -> list[str]:
        folded = text.casefold()
        return [term for term, pattern in patterns if term.casefold() in folded and pattern.search(text)]

    def screen(self, paper: Paper) -> dict:
        evidence = []
        title_topics = set()
        abstract_topics = set()
        for topic, patterns in self.patterns.items():
            for field, text, topics in (("title", paper.title, title_topics), ("abstract", paper.abstract, abstract_topics)):
                if not self.guards[topic].search(text):
                    continue
                matches = self.matches(patterns, text)
                if matches:
                    topics.add(topic)
                    evidence.append({"field": field, "topic": topic, "terms": matches})
        def extra(name, text):
            return self.matches(self.extra_patterns[name], text) if self.guards[name].search(text) else []
        broad = extra("broad_review", paper.title + " " + paper.abstract)
        biological = extra("pure_biology", paper.title)
        rescue = extra("clinical_rescue", paper.title) if biological else []
        if biological and not rescue:
            decision = "out_of_scope"
        elif title_topics:
            decision = "candidate"
        elif abstract_topics or broad:
            decision = "review"
        else:
            decision = "not_flagged"
        if broad:
            evidence.append({"field": "title_or_abstract", "topic": "broad_review", "terms": broad})
        if biological:
            evidence.append({"field": "title", "topic": "pure_biology", "terms": biological})
        score = min(100, 60 * bool(title_topics) + 10 * min(3, len(title_topics)) + 5 * min(3, len(abstract_topics)) + 5 * bool(broad))
        excerpt = ""
        if paper.abstract:
            offset = 0
            for topic in self.patterns:
                found = self.guards[topic].search(paper.abstract)
                if found:
                    offset = max(0, found.start() - 100)
                    break
            excerpt = ("…" if offset else "") + paper.abstract[offset:offset + 440] + ("…" if len(paper.abstract) > offset + 440 else "")
        return {"decision": decision, "score": score, "topics": sorted(title_topics | abstract_topics),
                "evidence": evidence, "abstract_excerpt": excerpt, "abstract_available": bool(paper.abstract)}


def reconcile(papers: list[Paper], readme: list[dict]) -> tuple[dict[str, dict], list[dict]]:
    titles: dict[str, list[dict]] = defaultdict(list)
    urls: dict[str, list[dict]] = defaultdict(list)
    editions = defaultdict(list)
    for entry in readme:
        normalized = key(entry["title"])
        titles[normalized].append(entry)
        # Reuse the second-sequence index for the expanded README. The quick
        # ratios are upper bounds, so pruning preserves the 0.90 match rule.
        editions[(entry["venue"], entry["year"])].append(
            (entry, SequenceMatcher(None, "", normalized)))
        if is_paper_url(entry["url"]):
            urls[canonical_url(entry["url"])].append(entry)
    matched_lines = set()
    matches = {}
    for paper in papers:
        exact = titles.get(key(paper.title), [])
        method = "title"
        url_conflicts = []
        if not exact:
            # A wrong README link must not hide a genuinely unlisted paper.
            # Different titles sharing a URL remain a visible review conflict.
            url_conflicts = [entry for url in [paper.url, *paper.alternate_urls] if is_paper_url(url)
                             for entry in urls.get(canonical_url(url), [])]
        if exact:
            matched_lines.update(entry["line"] for entry in exact)
            matches[paper.identity] = {"status": "already_listed", "match_method": method,
                                       "readme_lines": sorted({entry["line"] for entry in exact}),
                                       "placement_mismatch": any(entry["venue"] != paper.venue or entry["year"] != paper.year for entry in exact)}
        else:
            similar = []
            normalized = key(paper.title)
            for entry, matcher in editions[(paper.venue, paper.year)]:
                matcher.set_seq1(normalized)
                if matcher.real_quick_ratio() < 0.90 or matcher.quick_ratio() < 0.90:
                    continue
                # Preserve the original argument order for SequenceMatcher's
                # tie-breaking behavior on the final exact similarity score.
                ratio = SequenceMatcher(None, key(entry["title"]), normalized).ratio()
                if ratio >= 0.90:
                    similar.append({"title": entry["title"], "line": entry["line"], "similarity": round(ratio, 3)})
            for entry in url_conflicts:
                if entry["line"] not in {item["line"] for item in similar}:
                    similar.append({"title": entry["title"], "line": entry["line"], "reason": "same URL, different title"})
            matches[paper.identity] = {"status": "possible_match" if similar else "not_listed", "possible_matches": similar,
                                       "url_title_conflicts": [{"title": e["title"], "line": e["line"]} for e in url_conflicts]}
    unmatched = [entry for entry in readme if entry["line"] not in matched_lines]
    return matches, unmatched


def parse_abstract(document: str) -> str:
    tree = soup(document)
    # These selectors exclude references, navigation, author affiliations, and
    # the rest of the page, which would create spurious medical matches.
    for selector in ('meta[name="citation_abstract"]', 'meta[name="DC.Description"]', 'meta[name="dc.Description"]',
                     "#abstract", "section.item.abstract", "div.item.abstract", "div.abstract", "p.abstract"):
        node = tree.select_one(selector)
        if node:
            value = node.get("content") or node.get_text(" ", strip=True)
            value = re.sub(r"^Abstract\s*", "", clean(value), flags=re.I)
            if len(value) > 100:
                return value
    header = tree.find(["h2", "h3", "h4"], string=re.compile(r"^\s*Abstract\s*$", re.I))
    if header:
        chunks = []
        for node in header.next_siblings:
            if getattr(node, "name", None) in ("h2", "h3", "h4"):
                break
            if getattr(node, "name", None) in ("p", "div"):
                chunks.append(node.get_text(" ", strip=True))
        value = clean(" ".join(chunks))
        if len(value) > 100:
            return value
    return ""


def enrich_missing(papers: list[Paper], rules: Rules, client: Client, mode: str, workers: int) -> list[dict]:
    failures = []
    selected = [p for p in papers if not p.abstract and is_paper_url(p.url)
                and (mode == "all" or (mode == "candidates" and rules.screen(p)["decision"] in ("candidate", "review")))]
    if mode == "none":
        return failures
    print(f"Fetching missing abstracts for {len(selected):,} accessible papers ({mode} mode).", flush=True)

    def fetch(paper: Paper):
        if "doi.org" in paper.url:
            doi = paper.url.split("doi.org/", 1)[1]
            source = f"https://api.crossref.org/works/{doi}"
            obj = json.loads(client.get(source))["message"]
            abstract = clean(soup(obj.get("abstract", "")).get_text(" "))
        else:
            source = paper.url
            abstract = parse_abstract(client.get(source))
        return paper, abstract, source

    with ThreadPoolExecutor(max_workers=workers) as pool:
        jobs = {pool.submit(fetch, p): p for p in selected}
        for completed, future in enumerate(as_completed(jobs), 1):
            paper = jobs[future]
            try:
                _, abstract, source = future.result()
                if abstract:
                    paper.abstract = abstract
                    paper.abstract_source = source
                    paper.sources = sorted(set(paper.sources + [source]))
                else:
                    failures.append({"id": paper.identity, "url": paper.url, "error": "No abstract in source metadata"})
            except Exception as exc:
                failures.append({"id": paper.identity, "url": paper.url, "error": str(exc)})
            if completed % 50 == 0 or completed == len(selected):
                print(f"Abstract pages checked: {completed:,}/{len(selected):,}; "
                      f"{len(failures):,} missing/failed.", flush=True)
    return sorted(failures, key=lambda row: row["id"])


def escape(value: str) -> str:
    return value.replace("<", "&lt;").replace(">", "&gt;").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def write_reports(papers: list[Paper], coverage: list[dict], rules: Rules, readme_path: Path,
                  data_dir: Path, report_dir: Path, client: Client, enrichment_failures: list[dict], options: dict,
                  curation: dict | None = None) -> dict:
    papers = sorted(papers, key=lambda p: (p.venue.casefold(), -p.year, key(p.title)))
    readme = read_readme(readme_path)
    matches, unmatched = reconcile(papers, readme)
    data_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    screened = []
    reviews = (curation or {}).get("reviewed", {})
    stale_curations = []
    full_temp, screened_temp = data_dir / ".papers.jsonl.tmp", data_dir / ".screened.jsonl.tmp"
    with full_temp.open("w", encoding="utf-8") as full, screened_temp.open("w", encoding="utf-8") as filtered:
        for paper in papers:
            row = {**paper.to_dict(), **rules.screen(paper), **matches[paper.identity]}
            review = reviews.get(paper.identity)
            if review:
                if any(review.get(field) != row[field] for field in ("title", "venue", "year", "track")):
                    stale_curations.append(paper.identity)
                else:
                    row["manual_decision"] = review["decision"]
                    row["manual_reason"] = review.get("reason", review.get("summary", ""))
            screened.append(row)
            full.write(json.dumps(paper.to_dict(), ensure_ascii=False) + "\n")
            filtered.write(json.dumps(row, ensure_ascii=False) + "\n")
    full_temp.replace(data_dir / "papers.jsonl")
    screened_temp.replace(data_dir / "screened.jsonl")
    by_edition = defaultdict(list)
    for row in screened:
        by_edition[(row["venue"], row["year"])].append(row)
    for edition in coverage:
        rows = by_edition[(edition["venue"], edition["year"])]
        edition["paper_count"] = len(rows)
        edition["abstract_count"] = sum(row["abstract_available"] for row in rows)
        edition["candidate_count"] = sum(row["decision"] == "candidate" for row in rows)
        edition["review_count"] = sum(row["decision"] == "review" for row in rows)
        edition["already_listed_count"] = sum(row["status"] == "already_listed" for row in rows)
    candidates = [r for r in screened if (r["decision"] in ("candidate", "review") or r.get("manual_decision") == "include")
                  and r["status"] != "already_listed" and r.get("manual_decision") != "exclude"]
    candidates.sort(key=lambda r: (r["decision"] != "candidate", r["venue"].casefold(), -r["year"], -r["score"], key(r["title"])))
    failed = [e for e in coverage if e["status"] == "failed"]
    report = {"generated_at": datetime.now(timezone.utc).isoformat(), "options": options,
              "rules_sha256": rules.sha256, "readme_sha256": hashlib.sha256(readme_path.read_bytes()).hexdigest(),
              "paper_count": len(papers), "abstract_count": sum(bool(p.abstract) for p in papers),
              "readme_paper_count": len(readme), "readme_matched_count": len(readme) - len(unmatched),
              "candidate_count": len(candidates), "decisions": dict(Counter(r["decision"] for r in screened)),
              "curation_counts": dict(Counter(r["manual_decision"] for r in screened if "manual_decision" in r)),
              "approved_unlisted_count": sum(r.get("manual_decision") == "include" for r in candidates),
              "stale_curations": stale_curations,
              "failed_editions": len(failed), "coverage": coverage, "unmatched_readme": unmatched,
              "placement_mismatches": [{"title": r["title"], "venue": r["venue"], "year": r["year"], "readme_lines": r["readme_lines"]} for r in screened if r.get("placement_mismatch")],
              "url_title_conflicts": [{"catalog_title": r["title"], "url": r["url"], "readme_entries": r["url_title_conflicts"]} for r in screened if r.get("url_title_conflicts")],
              "abstract_fetch_failures": enrichment_failures,
              "http_sources": sorted(client.used.values(), key=lambda r: r["url"])}
    (report_dir / "coverage.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with (report_dir / "candidates.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["venue", "year", "track", "title", "url", "decision", "manual_decision", "score", "status", "topics", "evidence", "abstract_available", "abstract_excerpt", "sources", "possible_matches"]
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in candidates:
            writer.writerow({k: json.dumps(row.get(k), ensure_ascii=False) if isinstance(row.get(k), (list, dict)) else row.get(k, "") for k in fields})
    lines = ["# Proceedings index coverage", "", f"Generated: {report['generated_at']}", "",
             f"Indexed **{len(papers):,} papers**; **{report['abstract_count']:,} have abstracts**. "
             f"Matched **{report['readme_matched_count']}/{len(readme)}** README entries. "
             f"Found **{len(candidates):,} unlisted candidates/review items**.", "",
             "This is a screening queue, not a list of accepted additions. Keyword screening cannot guarantee recall. "
             "All indexed papers, including unflagged and out-of-scope records, remain in `data/papers.jsonl` and `data/screened.jsonl`.", "",
             "An indexed catalog is not an independently verified total unless the count check says so. "
             "Missing abstracts, source failures, and accepted-list fallbacks remain explicit below and in `coverage.json`.", "",
             f"Manual review decisions in the selected catalogs: {report['curation_counts']}. "
             f"Approved but unlisted: {report['approved_unlisted_count']}. "
             f"Stale decisions requiring re-review: {len(stale_curations)}. "
             "Manually excluded records remain in the full index but are omitted from the pending queue.", "",
             "| Conference | Status | Papers | Abstracts | Candidates | Review | Already listed | Count check |",
             "|---|---|---:|---:|---:|---:|---:|---|"]
    for e in coverage:
        lines.append(f"| {e['venue']} {e['year']} | {e['status']} | {e.get('paper_count', 0)} | {e.get('abstract_count', 0)} | {e.get('candidate_count', 0)} | {e.get('review_count', 0)} | {e.get('already_listed_count', 0)} | {e.get('count_check', 'not_applicable')} |")
    lines += ["", "## Source notes", ""]
    for e in coverage:
        if e["status"] == "not_held":
            continue
        for note in [*e.get("notes", []), *([e["error"]] if e.get("error") else [])]:
            lines.append(f"- **{e['venue']} {e['year']}**: {escape(note)}")
    lines += ["", "## README entries not matched to the selected catalogs", "",
              "An unmatched entry is a review task, not proof that the paper is invalid: titles may change, "
              "a different track may be needed, or a source may have failed.", ""]
    for row in unmatched:
        lines.append(f"- {row['venue']} {row['year']}, README line {row['line']}: [{escape(row['title'])}]({row['url']})")
    lines += ["", "## Placement mismatches", ""]
    lines += [f"- [{escape(r['title'])}]({r['url']}): catalog {r['venue']} {r['year']}; README lines {r['readme_lines']}" for r in screened if r.get("placement_mismatch")]
    if not report["placement_mismatches"]:
        lines.append("None found among exact title/URL matches.")
    lines += ["", "## Same URL, different title", "",
              "These records remain in the review queue; a shared URL alone does not prove the paper is already listed.", ""]
    for conflict in report["url_title_conflicts"]:
        lines.append(f"- [{escape(conflict['catalog_title'])}]({conflict['url']}): README "
                     + "; ".join(f"line {e['line']}: {escape(e['title'])}" for e in conflict["readme_entries"]))
    if not report["url_title_conflicts"]:
        lines.append("None found among indexed paper-specific URLs.")
    (report_dir / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    lines = ["# Medical AI screening queue", "", "Generated automatically; review venue, scope, abstract, and link before adding to README. "
             "Scores are rule-based ranking signals, not relevance probabilities. "
             "`candidate` means the title matched a specific rule; `review` includes broad or abstract-only matches.", "",
             "See [coverage](coverage.md) for failures, catalog fallbacks, abstract coverage, and unmatched README entries. "
             "Possible duplicate matches are retained for human review. Explicit exclusions in "
             "[the curation ledger](../data/curation.json) are omitted; their full records remain in the index.", ""]
    for decision in ("candidate", "review", "out_of_scope", "not_flagged"):
        selected = [r for r in candidates if r["decision"] == decision]
        if decision not in ("candidate", "review") and not selected:
            continue
        heading = {"candidate": "Title-matched candidates", "review": "Broader and abstract-only review"}.get(decision, "Manually approved rule overrides: " + decision)
        lines += [f"## {heading}", ""]
        previous = None
        for row in selected:
            group = (row["venue"], row["year"])
            if group != previous:
                lines += [f"### {row['venue']} {row['year']}", ""]
                previous = group
            evidence = "; ".join(f"{e['field']}: {', '.join(e['terms'])}" for e in row["evidence"])
            lines += [f"- **[{escape(row['title'])}]({row['url']})** — {row['track']}; score {row['score']}; {row['status']}",
                      f"  - Matches: {escape(evidence)}"]
            if row["abstract_excerpt"]:
                lines.append(f"  - Abstract excerpt: {escape(row['abstract_excerpt'])}")
            else:
                lines.append("  - Abstract unavailable; title-only screening.")
            if row.get("possible_matches"):
                lines.append(f"  - Possible README duplicate: {escape('; '.join(p['title'] for p in row['possible_matches']))}")
        lines.append("")
    (report_dir / "candidates.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return report
