#!/usr/bin/env python3
"""Retrieve candidates for methodological science; render separately reviewed notes.

Scores prioritize reading, never assign contribution types. No network access.
The reviewed ledger can be rendered without the ignored full proceedings index.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re

from paper_index.pipeline import Rules, read_readme
from paper_index.sources import Paper, key

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    "data_and_transfer": "Data, representation, and transfer assumptions",
    "evaluation": "Evaluation validity, shortcuts, and clinical utility",
    "method_hybrid": "Problem discovery with a substantial method contribution",
    "position": "Position papers with supporting empirical studies",
}


def load_json(path):
    return json.loads(path.read_text())


def identity(row):
    return row["venue"], row["year"], key(row["title"])


def score_paper(paper, config):
    """Count each cue once per field, so repeated keywords cannot inflate scores."""
    total, reasons = 0, []
    for rule in config["patterns"]:
        fields = ("title",) if rule.get("title_only") else ("title", "abstract")
        for field in fields:
            if re.search(rule["pattern"], paper.get(field, ""), re.I):
                total += rule["weight"]
                reasons.append(f"{field}:{rule['name']}")
    return total, reasons


def retrieve(papers, curated, ledger, config, medical_rules):
    approved = {identity(r): r for r in ledger["papers"]}
    candidates = []
    for paper in papers:
        ident = identity(paper)
        reviewed = approved.get(ident)
        score, reasons = score_paper(paper, config)
        # A question title alone merits reading, including low-score studies.
        title_cue = "title:title_question_or_study" in reasons
        if not reviewed and score < config["minimum_score"] and not title_cue:
            continue
        medical_status = "curated" if ident in curated else ""
        if not medical_status and not reviewed:
            fields = {k: paper[k] for k in Paper.__dataclass_fields__ if k in paper}
            medical_status = medical_rules.screen(Paper(**fields))["decision"]
            if medical_status not in {"candidate", "review"}:
                continue
        candidates.append({
            "id": paper["id"], "venue": paper["venue"], "year": paper["year"],
            "track": paper.get("track", ""), "title": paper["title"], "url": paper["url"],
            "abstract_available": bool(paper.get("abstract")), "already_curated": ident in curated,
            "retrieval_score": score, "retrieval_reasons": ";".join(reasons),
            "medical_screen": medical_status or "reviewed_ledger",
            "review_status": "reviewed_for_guide" if reviewed else "unreviewed_candidate",
        })
    found = {(r["venue"], r["year"], key(r["title"])) for r in candidates}
    missing = set(approved) - found
    if missing:
        raise ValueError(f"Reviewed papers absent from index: {sorted(missing)}")
    return sorted(candidates, key=lambda r: (-r["retrieval_score"], -r["year"], r["venue"], r["title"]))


def validate_ledger(ledger):
    seen = set()
    for row in ledger["papers"]:
        ident = identity(row)
        if ident in seen:
            raise ValueError(f"Duplicate reviewed paper: {ident}")
        seen.add(ident)
        if row["group"] not in GROUPS:
            raise ValueError(f"Unknown group: {row['group']}")
        for field in ("question", "finding", "evidence", "scope", "evidence_location", "url", "track"):
            if not row.get(field):
                raise ValueError(f"Missing {field}: {row['title']}")
        if row["review_level"] not in {"abstract_checked", "selected_fulltext_sections"}:
            raise ValueError(f"Unknown review level: {row['review_level']}")
        if row["review_level"] == "selected_fulltext_sections" and not all(
            row.get(k) for k in ("pdf_url", "pdf_sha256")
        ):
            raise ValueError(f"Full-text review needs source fingerprint: {row['title']}")


def render_guide(ledger):
    validate_ledger(ledger)
    rows = ledger["papers"]
    full = sum(r["review_level"] == "selected_fulltext_sections" for r in rows)
    lines = [
        "# Medical AI: problem-discovery reading guide", "",
        "Studies of where existing algorithms, training practices, or evaluation assumptions fail in medical AI, sometimes followed by a corrective method. Here, **science** means methodological discovery, rather than discovery of a biological mechanism. A new architecture or an improved benchmark score alone does not meet this definition.", "",
        f"This selected guide contains **{len(rows)} papers**. {full} have checks of selected full-text sections; the remainder are abstract-level recommendations. These are reading notes, not independent replications or a complete census.", "",
        "Science, methods, and benchmarks can overlap. Contribution tags are editorial judgments. A benchmark is included when it supports a specific diagnosis of an existing practice; position papers and method-heavy hybrids are separated below. Evidence and limitations are recorded for each entry. Publication years and tracks follow official proceedings.", "",
        "[Back to the awesome list](../../README.md) · [Machine-readable review ledger](../../data/science_review.json) · [Candidate queue](candidates.csv) · [Retrieval provenance](retrieval-summary.json)", "",
        "## How to use this guide", "",
        "Read the question and finding first, then check the evidence and scope before generalizing. ‘Selected full-text sections’ means the cited passages were inspected, not that every experiment or supplement was audited. ‘Abstract checked’ requires deeper reading before relying on detailed mechanisms. Main-list membership is noted separately from inclusion in this guide.", "",
    ]
    for group, label in GROUPS.items():
        lines += [f"## {label}", ""]
        for row in (r for r in rows if r["group"] == group):
            in_list = "in main list" if row["already_curated"] else "indexed; not yet in main list"
            track = "position paper (combined proceedings volume)" if group == "position" else row["track"]
            review = row['review_level'].replace('_', ' ').replace('fulltext', 'full-text')
            pdf_link = f" [Reviewed PDF]({row['pdf_url']})." if row['review_level'] == 'selected_fulltext_sections' else ""
            lines += [
                f"### {row['venue']} {row['year']} — {row['title']}", "",
                f"[Official paper]({row['url']}) · {track} · {', '.join(row['contribution_tags'])} · {in_list}.", "",
                f"**Question:** {row['question']}", "",
                f"**Finding:** {row['finding']}", "",
                f"**Evidence / intervention:** {row['evidence']}", "",
                f"**Scope:** {row['scope']}", "",
                f"**Review:** {review}; {row['evidence_location']}.{pdf_link}", "",
            ]
    lines += [
        "## Reproduce and extend", "",
        "Render these reviewed notes without downloading the proceedings:", "",
        "```sh", "python scripts/find_science_papers.py --render-only", "```", "",
        "After rebuilding the local proceedings index using the indexing instructions in the main README, rerun candidate retrieval:", "",
        "```sh", "python scripts/find_science_papers.py", "```", "",
        "Retrieval uses title/abstract cues plus the existing medical-scope rules and curated identities. Each output retains conference, publication year, and track. Reviewed ledger entries are retained even if they score poorly. Scores only prioritize reading; an unreviewed candidate is **not** an accepted science classification. False positives, missing abstracts, and papers without the cue vocabulary remain possible. This search does not establish exhaustive recall.", "",
        "To extend the guide, read the official source and add the question, finding, evidence location, and limits to `data/science_review.json`. Record whether only the abstract or selected full-text passages were inspected. PDF hashes identify the reviewed version; raw PDFs and extracted text stay in the ignored cache. The ledger's main-list membership is a snapshot of its review date.", "",
        "This purposive selection cannot estimate the fraction of science versus engineering papers, changes in that fraction by year, or acceptance probabilities. Those require a systematically labeled denominator; acceptance analysis also needs rejected submissions.", "",
        f"Reviewed: {ledger['reviewed_on']}. Generated by `scripts/find_science_papers.py`; edit the ledger rather than this file.", "",
    ]
    return "\n".join(lines)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, default=ROOT / "data/papers.jsonl")
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--ledger", type=Path, default=ROOT / "data/science_review.json")
    parser.add_argument("--config", type=Path, default=ROOT / "config/science_retrieval.json")
    parser.add_argument("--medical-rules", type=Path, default=ROOT / "config/medical_topics.json")
    parser.add_argument("--output", type=Path, default=ROOT / "reports/science")
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()
    ledger = load_json(args.ledger)
    guide = render_guide(ledger)
    args.output.mkdir(parents=True, exist_ok=True)
    if not args.render_only:
        if not args.papers.exists():
            parser.error("Build data/papers.jsonl first, or use --render-only.")
        papers = [json.loads(line) for line in args.papers.read_text().splitlines() if line.strip()]
        config = load_json(args.config)
        rules = Rules(args.medical_rules)
        candidates = retrieve(papers, {identity(r) for r in read_readme(args.readme)}, ledger, config, rules)
        fields = ["id", "venue", "year", "track", "title", "url", "abstract_available", "already_curated",
                  "retrieval_score", "retrieval_reasons", "medical_screen", "review_status"]
        with (args.output / "candidates.csv").open("w", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=fields)
            writer.writeheader()
            writer.writerows(candidates)
        summary = {
            "input_sha256": {name: sha256(path) for name, path in {
                "papers": args.papers, "readme": args.readme, "ledger": args.ledger,
                "retrieval_config": args.config, "medical_rules": args.medical_rules,
                "retrieval_script": Path(__file__),
            }.items()},
            "indexed_records": len(papers), "indexed_with_abstract": sum(bool(r.get("abstract")) for r in papers),
            "candidate_records": len(candidates), "candidate_with_abstract": sum(r["abstract_available"] for r in candidates),
            "candidate_by_year": dict(sorted(Counter(r["year"] for r in candidates).items())),
            "candidate_by_review_status": dict(sorted(Counter(r["review_status"] for r in candidates).items())),
            "warning": "Retrieval scores are not contribution labels. Selection is purposive, with unknown recall; no population proportions or acceptance rates follow from this queue.",
        }
        (args.output / "retrieval-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        print(f"Retrieved {len(candidates)} candidates; {len(ledger['papers'])} reviewed guide entries.")
    (args.output / "README.md").write_text(guide)


if __name__ == "__main__":
    main()
