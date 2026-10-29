#!/usr/bin/env python3
"""Generate conference shares, topic trends, ICLR comparisons, CSVs, and figures."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path

from paper_index.research import (TopicRules, acceptance_analysis, analyse, eligible,
                                  pct, write_csv, write_reports)
from paper_index.sources import key

ROOT = Path(__file__).resolve().parents[1]


def figures(result, rates, out):
    os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "svg.fonttype": "none", "svg.hashsalt": "medical-ai-research-v1",
                         "axes.spines.top": False, "axes.spines.right": False,
                         "figure.facecolor": "#ffffff", "axes.facecolor": "#ffffff",
                         "axes.titleweight": "bold", "axes.labelcolor": "#334155"})
    out.mkdir(parents=True, exist_ok=True)
    def save(fig, name):
        svg_path = out / (name + ".svg")
        fig.savefig(svg_path, bbox_inches="tight", metadata={"Date": None})
        svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n")
        fig.savefig(out / (name + ".png"), dpi=180, bbox_inches="tight")
        plt.close(fig)
    fig, ax = plt.subplots(figsize=(8, 4.3))
    rows = result["yearly"]
    bars = ax.bar([str(r["year"]) for r in rows], [r["curated_share_pct"] for r in rows], color=["#94a3b8", "#38bdf8", "#0d9488"], width=.5)
    for bar, row in zip(bars, rows):
        ax.annotate(f"{row['curated_share_pct']:.2f}%\n{row['curated_medical_records']:,} / {row['eligible_research_records']:,}", (bar.get_x()+bar.get_width()/2, bar.get_height()), xytext=(0, 6), textcoords="offset points", ha="center")
    ax.set_ylim(0, max(r["curated_share_pct"] for r in rows)*1.4)
    ax.set_ylabel("Curated medical papers / eligible indexed papers (%)")
    ax.set_title("Medical AI in conference proceedings, 2023–2025", loc="left", pad=20)
    fig.text(.12, -.02, "Observed lower-bound curated shares • Not submission acceptance rates", color="#475569", fontsize=9)
    save(fig, "medical-share")
    venues = sorted({r["venue"] for r in result["shares"]})
    data = np.full((len(venues), 3), np.nan)
    for row in result["shares"]:
        data[venues.index(row["venue"]), row["year"]-2023] = row["curated_share_of_eligible_pct"]
    fig, ax = plt.subplots(figsize=(7.5, 7))
    im = ax.imshow(data, cmap="YlGnBu", aspect="auto", vmin=0)
    ax.set_xticks(range(3), ["2023", "2024", "2025"])
    ax.set_yticks(range(len(venues)), venues)
    for i in range(len(venues)):
        for j in range(3):
            v = data[i, j]
            ax.text(j, i, "Not held" if np.isnan(v) else f"{v:.2f}%", ha="center", va="center", color="white" if v>4.5 else "#172554")
    ax.set_title("Curated medical share by conference and year", loc="left", pad=15)
    fig.colorbar(im, ax=ax, label="Share of eligible indexed papers (%)")
    save(fig, "conference-shares")
    for family, filename in (("domain", "topic-trends"), ("method", "method-trends")):
        rows = [r for r in result["topics"] if r["family"] == family]
        names = sorted({r["topic"] for r in rows}, key=lambda n: -sum(r["papers"] for r in rows if r["topic"]==n))
        fig, ax = plt.subplots(figsize=(11, max(5, len(names)*.43)))
        y = np.arange(len(names))
        for k, (year, color) in enumerate(zip((2023, 2024, 2025), ("#94a3b8", "#38bdf8", "#0d9488"))):
            lookup = {r["topic"]:r["share_of_medical_pct"] for r in rows if r["year"]==year}
            ax.barh(y+(k-1)*.24, [lookup[n] for n in names], height=.22, label=str(year), color=color)
        ax.set_yticks(y, names)
        ax.invert_yaxis()
        ax.set_xlabel("Share of that year's curated medical papers (%) • Multi-label title rules")
        ax.legend(frameon=False, loc="lower right")
        ax.set_title("Research domains" if family=="domain" else "Research methods", loc="left", pad=15)
        save(fig, filename)
    if rates:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        for group, offset, color, label in (("medical_keyword", -.1, "#0d9488", "Specific medical-title keyword match"), ("other_titles", .1, "#64748b", "Other titles (may include missed medical papers)")):
            rows = sorted((r for r in rates if r["definition"]=="specific_title_proxy" and r["group"]==group), key=lambda r:r["year"])
            selected = [r for r in rows if r["decision_rate_pct"] is not None]
            ax.errorbar([r["year"]+offset for r in selected], [r["decision_rate_pct"] for r in selected],
                        yerr=[[r["decision_rate_pct"]-r["wilson95_low_pct"] for r in selected], [r["wilson95_high_pct"]-r["decision_rate_pct"] for r in selected]],
                        marker="o", capsize=4, color=color, label=label)
        ax.set_xticks([2023, 2024, 2025])
        ax.set_ylabel("Accepted / (accepted + rejected decisions), %")
        ax.set_title("ICLR decision rates by title-keyword group", loc="left", pad=15)
        ax.legend(frameon=False, fontsize=8, loc="lower left")
        fig.text(.12, -.035, "Historical third-party OpenReview snapshots • 95% Wilson intervals • Not causal evidence", fontsize=8, color="#475569")
        save(fig, "iclr-decision-rates")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, default=ROOT / "data/papers.jsonl")
    parser.add_argument("--submissions", type=Path, default=ROOT / "data/submissions.jsonl")
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--rules", type=Path, default=ROOT / "config/research_topics.json")
    parser.add_argument("--output", type=Path, default=ROOT / "reports/analysis")
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args()
    if not args.submissions.exists():
        parser.error("Submission data missing: run python scripts/fetch_submissions.py --source snapshot first. Accepted-only data cannot identify acceptance rates.")
    papers = [json.loads(line) for line in args.papers.open(encoding="utf-8")]
    if len({p["id"] for p in papers}) != len(papers):
        raise ValueError("Duplicate catalog identities")
    rules = TopicRules(json.loads(args.rules.read_text()))
    result = analyse(papers, args.readme, rules)
    submissions = [json.loads(line) for line in args.submissions.open(encoding="utf-8")] if args.submissions.exists() else []
    rates, areas, annotations, validation = acceptance_analysis(submissions, papers, rules)
    baselines = json.loads((ROOT / "config/conference_statistics.json").read_text())["official_baselines"]
    paths = [args.papers, args.readme, args.rules, ROOT / "config/conference_statistics.json"]
    if args.submissions.exists():
        paths.append(args.submissions)
    provenance = {"input_sha256": {str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                  "corpus": "Exact normalized README title + conference + publication-year join; title-only topic and keyword analysis",
                  "snapshot_fetcher": "scripts/fetch_submissions.py", "submission_rows": len(submissions),
                  "missing_submission_data": not bool(submissions)}
    write_reports(result, rates, areas, validation, baselines, args.output, provenance)
    if annotations:
        write_csv(args.output / "submission_annotations.csv", annotations, list(annotations[0]))
    keys = {(p["venue"], p["year"], key(p["title"])) for p in result["annotated"]}
    tracks = defaultdict(lambda: [0, 0, False])
    for p in papers:
        t = tracks[(p["venue"], p["year"], p["track"])]
        t[0] += 1
        t[1] += (p["venue"], p["year"], key(p["title"])) in keys
        t[2] = eligible(p)
    track_rows = [{"venue": v, "year": y, "track": t, "catalog_records": n, "curated_medical_records": m,
                   "eligible_research": e, "curated_share_pct": pct(m,n)} for (v,y,t),(n,m,e) in sorted(tracks.items())]
    write_csv(args.output / "track_shares.csv", track_rows, list(track_rows[0]))
    if not args.no_plots:
        figures(result, rates, args.output / "figures")
    print(json.dumps({"curated": len(result["annotated"]), "yearly": result["yearly"], "ICLR_validation": validation}, indent=2))


if __name__ == "__main__":
    main()
