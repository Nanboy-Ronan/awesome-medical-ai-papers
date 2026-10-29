"""Reproducible descriptive research; shares and decision rates stay separate."""

from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import re

from .pipeline import read_readme
from .sources import key


YEARS = (2023, 2024, 2025)


def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pct(n, d):
    return 100 * n / d if d else None


def display(value):
    return "N/A" if value is None else f"{value:.2f}%"


def eligible(paper):
    """Exclude mixed-volume short formats; keep research and benchmark tracks."""
    if paper["venue"] == "AAAI":
        track = paper["track"]
        return track.startswith(("AAAI Technical Track", "AAAI Special Track")) or track == "Intelligent Robots (ROB)"
    return paper["track"] not in ("findings", "industry", "demo", "workshop")


class TopicRules:
    def __init__(self, config):
        self.config = config
        self.domains = {name: [re.compile(p, re.I) for p in patterns] for name, patterns in config["domains"].items()}
        self.methods = {name: [re.compile(p, re.I) for p in patterns] for name, patterns in config["methods"].items()}
        self.medical = re.compile("|".join(f"(?:{p})" for p in config["medical_proxy_patterns"]), re.I)
        self.broad = re.compile("|".join(f"(?:{p})" for p in config["broad_proxy_patterns"]), re.I)
        self.false = re.compile("|".join(f"(?:{p})" for p in config["false_positive_patterns"]), re.I)
        self.stop = set(config["stopwords"].split())
        self.phrase_stop = self.stop - set(config.get("phrase_stopword_exceptions", []))

    def labels(self, title, family):
        rules = self.domains if family == "domain" else self.methods
        return [name for name, patterns in rules.items() if any(p.search(title) for p in patterns)]

    def medical_proxy(self, title, broad=False):
        if self.false.search(title):
            return False
        return bool(self.medical.search(title) or (broad and self.broad.search(title)))

    def keywords(self, title):
        # Document frequency: repeated mentions within one title count once.
        tokens = re.findall(r"[a-z][a-z0-9]+", title.casefold().replace("-", " "))
        unigrams = {t for t in tokens if len(t) >= 3 and t not in self.stop}
        bigrams = {a + " " + b for a, b in zip(tokens, tokens[1:])
                   if a not in self.phrase_stop and b not in self.phrase_stop and len(a) >= 3 and len(b) >= 3}
        return unigrams | bigrams


def wilson(accepted, total, z=1.95996398454):
    if not total:
        return None, None
    p = accepted / total
    denom = 1 + z*z/total
    center = (p + z*z/(2*total)) / denom
    radius = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total)) / denom
    return 100 * (center-radius), 100 * (center+radius)


def decision_row(rows, venue, year, group, definition):
    counts = Counter(row["status"] for row in rows)
    a, r = counts["accepted"], counts["rejected"]
    low, high = wilson(a, a+r)
    return {"venue": venue, "year": year, "group": group, "definition": definition,
            "accepted": a, "rejected": r, "desk_rejected": counts["desk_rejected"],
            "withdrawn": counts["withdrawn"], "unknown": counts["unknown"],
            "decision_denominator": a+r, "decision_rate_pct": pct(a, a+r),
            "wilson95_low_pct": low, "wilson95_high_pct": high,
            "observed_pool_denominator": len(rows), "accepted_fraction_observed_pool_pct": pct(a, len(rows))}


def aggregate_shares(papers, curated_keys):
    groups = defaultdict(list)
    for paper in papers:
        groups[(paper["venue"], paper["year"])].append(paper)
    result = []
    for (venue, year), rows in sorted(groups.items()):
        research = [r for r in rows if eligible(r)]
        medical = [r for r in rows if (venue, year, key(r["title"])) in curated_keys]
        research_medical = [r for r in medical if eligible(r)]
        result.append({"venue": venue, "year": year, "catalog_records": len(rows),
                       "eligible_research_records": len(research), "curated_medical_records": len(medical),
                       "curated_eligible_medical": len(research_medical),
                       "curated_share_of_catalog_pct": pct(len(medical), len(rows)),
                       "curated_share_of_eligible_pct": pct(len(research_medical), len(research)),
                       "count_basis": "Indexed catalog / accepted-list snapshot; curated share is an observed lower bound, not an acceptance rate"})
    return result


def analyse(papers, readme_path, rules):
    curated = read_readme(readme_path)
    curated_keys = {(r["venue"], r["year"], key(r["title"])) for r in curated}
    if len(curated_keys) != len(curated):
        raise ValueError("Duplicate README entries")
    by_key = {(r["venue"], r["year"], key(r["title"])): r for r in papers}
    if not curated_keys <= by_key.keys():
        raise ValueError("Some curated papers cannot be aligned to indexed conference/year metadata")
    annotated = []
    for entry in curated:
        paper = by_key[(entry["venue"], entry["year"], key(entry["title"]))]
        annotated.append({"id": paper["id"], "venue": entry["venue"], "year": entry["year"],
                          "title": paper["title"], "url": entry["url"], "track": paper["track"],
                          "domains": "; ".join(rules.labels(paper["title"], "domain")),
                          "methods": "; ".join(rules.labels(paper["title"], "method")),
                          "abstract_available": bool(paper.get("abstract")), "eligible_research": eligible(paper)})
    shares = aggregate_shares(papers, curated_keys)
    yearly = []
    for year in YEARS:
        rows = [r for r in shares if r["year"] == year]
        d, m = sum(r["eligible_research_records"] for r in rows), sum(r["curated_eligible_medical"] for r in rows)
        yearly.append({"year": year, "catalog_records": sum(r["catalog_records"] for r in rows),
                       "eligible_research_records": d, "curated_medical_records": m,
                       "curated_share_pct": pct(m, d), "held_editions": len(rows)})
    topics = []
    for year in YEARS:
        rows = [r for r in annotated if r["year"] == year]
        for family, field, names in (("domain", "domains", rules.domains), ("method", "methods", rules.methods)):
            for name in names:
                n = sum(name in r[field].split("; ") for r in rows)
                topics.append({"year": year, "family": family, "topic": name, "papers": n,
                               "year_medical_papers": len(rows), "share_of_medical_pct": pct(n, len(rows))})
    counts = {year: Counter() for year in YEARS}
    sizes = Counter(r["year"] for r in annotated)
    for r in annotated:
        counts[r["year"]].update(rules.keywords(r["title"]))
    vocab = set().union(*(c.keys() for c in counts.values()))
    keywords = []
    for term in sorted(vocab):
        if sum(counts[y][term] for y in YEARS) < 5:
            continue
        for year in YEARS:
            keywords.append({"year": year, "keyword": term, "papers": counts[year][term],
                             "year_medical_papers": sizes[year], "document_frequency_pct": pct(counts[year][term], sizes[year]),
                             "ngram": 2 if " " in term else 1})
    changes = []
    for term in sorted(vocab):
        a, b = counts[2023][term], counts[2025][term]
        if a+b < 8 or b < 5:
            continue
        start, end = pct(a, sizes[2023]), pct(b, sizes[2025])
        changes.append({"keyword": term, "papers_2023": a, "papers_2025": b,
                        "share_2023_pct": start, "share_2025_pct": end, "change_percentage_points": end-start})
    changes.sort(key=lambda r: (-r["change_percentage_points"], r["keyword"]))
    label_coverage = []
    for year in YEARS:
        rows = [r for r in annotated if r["year"] == year]
        for family, field in (("domain", "domains"), ("method", "methods")):
            matched = sum(bool(r[field]) for r in rows)
            label_coverage.append({"year": year, "family": family, "matched_papers": matched,
                                   "unmatched_papers": len(rows)-matched, "medical_papers": len(rows),
                                   "matched_pct": pct(matched, len(rows))})
    # Equal weight per conference family; combine alternating ICCV/ECCV editions.
    balanced = []
    families = sorted({r["venue"] if r["venue"] not in ("ICCV", "ECCV") else "ICCV/ECCV" for r in shares})
    family_year = defaultdict(lambda: [0, 0])
    for row in shares:
        family = "ICCV/ECCV" if row["venue"] in ("ICCV", "ECCV") else row["venue"]
        bucket = family_year[(family, row["year"])]
        bucket[0] += row["curated_eligible_medical"]
        bucket[1] += row["eligible_research_records"]
    common = [f for f in families if all(family_year[(f, y)][1] for y in YEARS)]
    for year in YEARS:
        balanced.append({"year": year, "common_families": len(common),
                         "equal_weight_family_share_pct": sum(pct(*family_year[(f, year)]) for f in common)/len(common) if common else None})
    return {"annotated": annotated, "shares": shares, "yearly": yearly, "topics": topics,
            "keywords": keywords, "keyword_changes": changes, "balanced": balanced,
            "common_families": common, "label_coverage": label_coverage}


def acceptance_analysis(submissions, papers, rules):
    grouped = defaultdict(list)
    for row in submissions:
        grouped[(row["venue"], row["year"])].append(row)
    result, areas, annotations, validation = [], [], [], []
    index_titles = defaultdict(set)
    for p in papers:
        index_titles[(p["venue"], p["year"])].add(key(p["title"]))
    for (venue, year), rows in sorted(grouped.items()):
        if not any(r["status"] == "rejected" for r in rows):
            raise ValueError(f"{venue} {year}: no rejected submissions; accepted-only data cannot identify acceptance rates")
        ids = [r["id"] for r in rows]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate submission IDs")
        for broad in (False, True):
            definition = "broad_sensitivity" if broad else "specific_title_proxy"
            medical = [r for r in rows if rules.medical_proxy(r["title"], broad)]
            other = [r for r in rows if not rules.medical_proxy(r["title"], broad)]
            for group, selected in (("medical_keyword", medical), ("other_titles", other)):
                result.append(decision_row(selected, venue, year, group, definition))
        result.append(decision_row(rows, venue, year, "all_titles", "snapshot_baseline"))
        areas_grouped = defaultdict(list)
        for row in rows:
            area = row.get("area") or "not_reported"
            areas_grouped[str(area)].append(row)
            annotations.append({"id": row["id"], "venue": venue, "year": year, "title": row["title"],
                                "status": row["status"], "area": area, "url": row["url"],
                                "specific_medical_title_match": rules.medical_proxy(row["title"]),
                                "broad_title_match": rules.medical_proxy(row["title"], True)})
        for area, records in sorted(areas_grouped.items()):
            areas.append(decision_row(records, venue, year, area, "self_reported_area_not_harmonized_across_years"))
        accepted = [r for r in rows if r["status"] == "accepted"]
        matched = sum(key(r["title"]) in index_titles[(venue, year)] for r in accepted)
        validation.append({"venue": venue, "year": year, "snapshot_accepted": len(accepted),
                           "accepted_exact_title_matches_to_catalog": matched,
                           "accepted_title_match_pct": pct(matched, len(accepted)),
                           "indexed_catalog_papers": len(index_titles[(venue, year)]),
                           "unresolved_status": sum(r["status"] == "unknown" for r in rows)})
    return result, areas, annotations, validation


def table(headers, rows):
    def safe(v):
        return str(v).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|",
                       *("| " + " | ".join(safe(v) for v in row) + " |" for row in rows)])


def write_reports(result, rates, areas, validation, baselines, out, provenance):
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("medical_papers", result["annotated"]), ("conference_year_shares", result["shares"]),
                       ("yearly_shares", result["yearly"]), ("balanced_shares", result["balanced"]),
                       ("topic_trends", result["topics"]), ("keywords_by_year", result["keywords"]),
                       ("topic_label_coverage", result["label_coverage"]),
                       ("keyword_changes", result["keyword_changes"]), ("acceptance_rates", rates),
                       ("acceptance_by_area", areas), ("submission_validation", validation)):
        if rows:
            write_csv(out / (name + ".csv"), rows, list(rows[0]))
    summary = {"years": list(YEARS), "curated_papers": len(result["annotated"]),
               "yearly": result["yearly"], "balanced": result["balanced"], "common_families": result["common_families"],
               "topic_label_coverage": result["label_coverage"],
               "acceptance_rates": rates, "submission_validation": validation,
               "official_baselines": baselines, "provenance": provenance,
               "interpretation": "Descriptive snapshot, not evidence of review preference, causal effects, or exhaustive medical coverage."}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    share_table = table(["Year", "Curated medical", "Eligible indexed papers", "Observed medical share"],
                        [(r["year"], r["curated_medical_records"], r["eligible_research_records"], display(r["curated_share_pct"])) for r in result["yearly"]])
    detail = table(["Conference", "Year", "Curated medical", "All catalog records", "Eligible research", "Share of eligible research"],
                   [(r["venue"], r["year"], r["curated_eligible_medical"], r["catalog_records"], r["eligible_research_records"], display(r["curated_share_of_eligible_pct"])) for r in result["shares"]])
    shares_md = f"""# Medical AI papers as a share of conference proceedings, 2023–2025

The numerator is the curated medical AI list, aligned by exact normalized title,
conference, and publication year. The denominator is the indexed research
catalog for the same edition. These are **observed lower-bound shares of the
indexed corpus**, not complete estimates of every medical paper and not
acceptance rates. A positive trend can reflect curation coverage as well as
changes in published research.

{share_table}

![Observed curated medical shares by year](figures/medical-share.svg)

## Every indexed conference edition

{detail}

The CSV includes both all-catalog and research-only denominators. For AAAI,
research-only includes technical and special research tracks and the 2024
Intelligent Robots research section; it excludes student/doctoral abstracts,
faculty/senior presentations, journal track, demos, errata, and co-located
IAAI/EAAI. Research, applied-data-science, and datasets/benchmarks remain in KDD;
datasets/benchmarks remain in NeurIPS. Track-level counts are exported separately.
Do not compare a combined-track numerator to a main-track-only denominator.

![Conference-year shares](figures/conference-shares.svg)

## Venue-mix sensitivity

ICCV/ECCV alternate and NAACL was not held in 2023. The pooled total consequently
does not have a fixed venue mix. As a sensitivity analysis, combine ICCV/ECCV and
give each family present in all three years equal weight:

{table(["Year", "Common families", "Equal-weight mean share"], [(r['year'], r['common_families'], display(r['equal_weight_family_share_pct'])) for r in result['balanced']])}

Common families: {', '.join(result['common_families'])}. This sensitivity controls
family composition, not topic classification error or incomplete curation.

## Coverage and reproducibility

The denominator measures indexed published/accepted-list records, which can
differ from chair-reported accepts because of withdrawals, corrections, track
boundaries, and snapshot timing. See [source coverage](../coverage.md).
Not-held editions are omitted, never treated as zero-percent medical years.
Counts are publication records, not unique research projects; cross-venue
versions are not collapsed. No binomial confidence interval is assigned to
these descriptive census shares: classification and coverage are the main
uncertainties. Download [conference-year counts](conference_year_shares.csv),
[track counts](track_shares.csv), and [provenance](summary.json).
"""
    (out / "medical-share.md").write_text(shares_md.rstrip() + "\n", encoding="utf-8")
    comparisons = [r for r in rates if r["definition"] == "specific_title_proxy"]
    rates_table = table(["Year", "Title group", "Accept", "Reject", "Decision rate", "95% Wilson interval", "Withdraw", "Desk reject"],
                        [(r["year"], r["group"], r["accepted"], r["rejected"], display(r["decision_rate_pct"]),
                          f"{display(r['wilson95_low_pct'])}–{display(r['wilson95_high_pct'])}", r["withdrawn"], r["desk_rejected"]) for r in comparisons])
    official_table = table(["Conference", "Year", "Track", "Submissions", "Accepted", "Reported-count rate", "Primary source"],
                           [(r["venue"], r["year"], r["track"], r["submitted"], r["accepted"], display(pct(r["accepted"], r["submitted"])), f"[source]({r['source']})") for r in baselines])
    area_tables = []
    for year in (2024, 2025):
        selected = sorted((r for r in areas if r["year"] == year and r["group"] != "not_reported"),
                          key=lambda r: -r["decision_denominator"])[:10]
        area_tables += [f"### {year}: ten largest self-reported areas by final-decision count", "",
                        table(["Research area", "Accept", "Reject", "Conditional decision rate"],
                              [(r["group"], r["accepted"], r["rejected"], display(r["decision_rate_pct"])) for r in selected]), ""]
    sensitivity_table = table(["Year", "Rule definition", "Medical-keyword decision rate", "Other-title decision rate"],
                              [(year,definition,*(display(next(r["decision_rate_pct"] for r in rates if r["year"]==year and r["definition"]==definition and r["group"]==group)) for group in ("medical_keyword","other_titles")))
                               for year in YEARS for definition in ("specific_title_proxy","broad_sensitivity")])
    rates_md = f"""# Medical versus other-title acceptance rates: an ICLR snapshot study

**Scope: ICLR 2023–2025 public submission snapshots. This does not estimate
medical acceptance rates for every conference in the awesome list.** Other
conferences need complete topic-labeled submissions and decisions, not just
accepted proceedings or aggregate conference statistics.

Direct OpenReview note queries returned browser-verification HTML during this
study. For a reproducible, explicitly limited comparison, we used Paper Copilot's
[published dataset](https://github.com/papercopilot/paperlists), pinned to commit
`9fcfd1234879a8e5630b5116dde411ec143dd763`. It is a **third-party historical
snapshot of OpenReview**, not a live official census. Source URLs and response
checksums are in [submission provenance](submission_sources.json). The primary
[OpenReview retrieval documentation](https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-all-notes-for-submissions-reviews-rebuttals-etc)
explains status fields; the import script supports official API v2 when available.

## Consistent topic rule for accepted and rejected papers

Apply the same specific medical title-keyword rule to **all** submissions.
The curated accepted list is not used to label only the accepted side, which
would introduce outcome-dependent classification bias. `medical_keyword`
means a title matched the published rules; `other_titles` means it did not.
The latter can include medical papers missed by keywords and is not a
ground-truth nonmedical group. These estimates are classifier-dependent.

The primary denominator is **accepted + rejected final decisions**. Withdrawn,
desk-rejected, and unknown records are shown separately. Consequently these
rates are **conditional on receiving an accept/reject decision** and generally
exceed chair-reported accepted/submitted rates. The CSV also reports the
accepted fraction of the entire observed pool, including withdrawals and desk
rejections, and a second, broader keyword definition as sensitivity analyses.

{rates_table}

## Classification sensitivity

{sensitivity_table}

The broader rule changes which titles enter each group. It includes terms such
as brain, biomedical, microscopy, treatment, and survival, which can identify
additional health research but also generic or basic-science work. Neither rule
has a validated precision/recall estimate for rejected papers. The difference
between definitions is part of the result, not a reason to select a preferred
headline after seeing outcomes.

![ICLR medical-keyword versus other-title decision rates](figures/iclr-decision-rates.svg)

Wilson intervals quantify binomial sampling variability under that model;
they do not account for snapshot selection, missing records, topic-label errors,
or venue policy changes. These historical records are not a random sample from
all future submissions. No significance or causal claim about reviewer preference
is made. Compare within the same year, track, source, rule, and denominator.

## Official whole-conference baselines

{official_table}

Official numbers are retained separately rather than silently forcing the
snapshot or proceedings to agree. ICLR 2023's baseline is derived from the
explicit year-on-year count differences in the 2024 fact sheet. The fact sheet
counts and snapshot counts have different inclusion and timing conventions.

## Snapshot validation and other fields

{table(["Year", "Snapshot accepts", "Exact-title matches to catalog", "Catalog records", "Unknown status"], [(r['year'], r['snapshot_accepted'], r['accepted_exact_title_matches_to_catalog'], r['indexed_catalog_papers'], r['unresolved_status']) for r in validation])}

The 2023 `Top-5%` and `Top-25%` labels denote accepted presentation tiers; all
371 such titles were checked against the official accepted index before mapping
them to `accepted`. IDs, not titles, deduplicate submissions. Unrecognized
statuses stay unknown and never become implicit rejections. Title changes can
cause catalog validation mismatches; an unmatched title is not reclassified.

Self-reported research-area rates for 2024 and 2025 are available in
[acceptance_by_area.csv](acceptance_by_area.csv). Those categories change across
years and are not a mutually exclusive medical/nonmedical ontology. Missing
2023 areas are explicitly `not_reported`. The headline medical comparison uses
the stable title classifier instead of stitching incompatible area labels.
See [all rate definitions](acceptance_rates.csv),
[paper-level derived labels](submission_annotations.csv), and
[validation counts](submission_validation.csv).

{chr(10).join(area_tables)}
"""
    (out / "acceptance-rates.md").write_text(rates_md.rstrip() + "\n", encoding="utf-8")
    topic_tables = []
    for family in ("domain", "method"):
        names = sorted({r["topic"] for r in result["topics"] if r["family"] == family})
        lookup = {(r["topic"], r["year"]): r for r in result["topics"] if r["family"] == family}
        topic_tables += [f"## {'Research domains' if family == 'domain' else 'Methods and research approaches'}", "",
                         table(["Topic", "2023", "2024", "2025"], [(name, *(f"{lookup[(name,y)]['papers']} ({display(lookup[(name,y)]['share_of_medical_pct'])})" for y in YEARS)) for name in names]), ""]
    top_keywords = []
    for year in YEARS:
        selected = sorted((r for r in result["keywords"] if r["year"] == year), key=lambda r: (-r["papers"], r["keyword"]))[:15]
        top_keywords += [f"### {year}", "", table(["Keyword / phrase", "Papers", "Share of that year's curated medical papers"],
                                                 [(r["keyword"], r["papers"], display(r["document_frequency_pct"])) for r in selected]), ""]
    topic_md = """# What medical AI papers studied in 2023–2025

This study analyzes **titles of curated papers**, with publication years from
the proceedings. It uses transparent multi-label domain/method patterns and
document-frequency keywords. Every year uses the same text field and rules;
uneven abstract availability is not allowed to change the text input by year.

Each paper can have several domains and methods, so percentages need not sum
to 100%. A zero means no title matched that rule, not that no work on the topic
was published. Counts reflect this list's scope and curation coverage.

## Label coverage

{coverage_table}

![Research domains by year](figures/topic-trends.svg)

""".replace("{coverage_table}", table(["Year", "Label family", "At least one match", "No match", "Match coverage"],
                                      [(r["year"],r["family"],r["matched_papers"],r["unmatched_papers"],display(r["matched_pct"])) for r in result["label_coverage"]])) + "\n".join(topic_tables) + """
![Method shares by year](figures/method-trends.svg)

## Title keyword analysis

Lowercase titles, split hyphens, tokenize alphabetic/alphanumeric words, remove
the published stopword list, and count unigrams and adjacent non-stopword
bigrams once per paper. `large`, `model`, and `models` remain available inside
bigrams (for example, `large language` and `foundation models`) while remaining
unigram stopwords. No stemming or learned topic model is used. Terms with
fewer than five papers over the full period are omitted from the keyword CSV.
Generic list-wide terms such as `medical`, `learning`, and `segmentation` are
stopwords for exploratory keywords; segmentation remains a separate method.
Keyword extraction is exploratory and sensitive to naming conventions.

""" + "\n".join(top_keywords) + "\n## Largest increases in title frequency, 2023 → 2025\n\n" + table(
        ["Keyword / phrase", "2023 papers", "2025 papers", "2023 share", "2025 share", "Change (percentage points)"],
        [(r["keyword"], r["papers_2023"], r["papers_2025"], display(r["share_2023_pct"]), display(r["share_2025_pct"]), f"{r['change_percentage_points']:+.2f}") for r in result["keyword_changes"][:20]]) + """

This ranking requires at least eight papers across the two endpoint years and
at least five in 2025. It compares normalized shares, not just raw count growth.
Overlapping unigrams and bigrams are retained, so `language` and `language
models` can appear together; they are not independent signals.

## Interpretation and limits

Inspect domain trends and method trends separately: a paper can study pathology
using a vision-language foundation model. Domain and method growth are not
competing slices of one pie. Changes across three observed years do not establish
a long-run trend, clinical effectiveness, or a causal response to model releases.
The curated corpus does not cover all health research, specialist medical
conferences, or every broad candidate in the index. Quantitative topic assignments
use deterministic matching rules; corpus membership follows the repository's
recorded curation decisions, whose scope errors can propagate into this study.

Download [paper-level labels](medical_papers.csv), [topic counts](topic_trends.csv),
[yearly keywords](keywords_by_year.csv), and [normalized keyword changes](keyword_changes.csv).
"""
    (out / "topics.md").write_text(topic_md.rstrip() + "\n", encoding="utf-8")
    intro = """# Medical AI conference research, 2023–2025

Three reproducible analyses of the curated awesome list and its full proceedings
index. **Shares of published papers and submission acceptance rates have different
denominators.** The accepted-paper analysis covers all indexed conference editions;
the decision-rate comparison is restricted to ICLR public snapshots.

1. [Medical share of proceedings by conference and year](medical-share.md)
2. [Medical versus other-title acceptance rates, with source and denominator limits](acceptance-rates.md)
3. [Yearly research domains, methods, and title keywords](topics.md)

""" + share_table + """

## Reproduce

```sh
python -m pip install -r requirements-analysis.txt
python scripts/index_papers.py --abstracts candidates
python scripts/fetch_submissions.py --source snapshot
python scripts/analyze_research.py
```

Cached inputs support `--offline` for the first two steps. The analysis itself
does not make network requests. No classifier score changes the awesome list.
Pinned snapshot references, source checksums, input/rule hashes, and the exact
corpus definition are exported in [summary.json](summary.json) and
[submission_sources.json](submission_sources.json). Full raw responses and
submission JSONL remain local; derived counts and labels are committed.

See [methodology and limitations](../../docs/research-methodology.md) for track
alignment, denominator choices, classification sensitivity, and coverage gaps.
"""
    (out / "README.md").write_text(intro.rstrip() + "\n", encoding="utf-8")
