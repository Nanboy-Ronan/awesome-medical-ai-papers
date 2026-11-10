#!/usr/bin/env python3
"""Verify presentation labels against official exports and annotate the README."""

import argparse
from collections import Counter
import json
from pathlib import Path
from urllib.parse import urljoin

from paper_index.pipeline import read_readme
from paper_index.presentations import LABELS, accepted_highlights, apply_badges, iccv_program, identity, virtual_labels
from paper_index.sources import Client, FetchError, bulk_url, edition_exists, key

ROOT = Path(__file__).resolve().parents[1]


def collect(root, client):
    curated = {identity(r): r for r in read_readme(root / "README.md")}
    papers = {}
    coverage = []
    for venue in ("CVPR", "NeurIPS", "ICML", "ICLR", "ICCV", "ECCV"):
        for year in (2023, 2024, 2025):
            if not edition_exists(venue, year):
                continue
            url = bulk_url(venue, year)
            entry = {"venue": venue, "year": year, "sources": [], "matched_papers": 0}
            matched = set()

            def record(title, labels, evidence):
                ident = f"{venue}:{year}:{key(title)}"
                if ident not in curated:
                    return
                matched.add(ident)
                if not labels:
                    return
                target = papers.setdefault(ident, {**{k: curated[ident][k] for k in ("venue", "year", "title")},
                                                   "labels": [], "evidence": []})
                target["labels"] = [label for label in LABELS if label in set(target["labels"] + labels)]
                if evidence not in target["evidence"]:
                    target["evidence"].append(evidence)

            try:
                if venue == "ICCV" and year == 2023:
                    url = "https://iccv2023.thecvf.com/main.conference.program-107.php"
                    for title, labels in iccv_program(client.get(url)):
                        record(title, labels, {"source": url, "url": url, "session_type": "Orals" if labels else "Posters"})
                    entry["sources"].append(client.used[url])
                    entry["matched_papers"] = len(matched)
                    entry["curated_papers"] = sum(r["venue"] == venue and r["year"] == year for r in curated.values())
                    coverage.append(entry)
                    continue
                data = json.loads(client.get(url))
                rows = data["results"] if isinstance(data, dict) else data
                if isinstance(data, dict) and (data.get("next") or data.get("count", len(rows)) != len(rows)):
                    raise ValueError("Incomplete virtual export")
                for row in rows:
                    if (row.get("eventtype") or "").casefold() not in ("oral", "poster", "spotlight"):
                        continue
                    labels = virtual_labels(row, venue, year)
                    proof = {"source": url, "url": urljoin(url, row.get("virtualsite_url") or url),
                             "decision": row.get("decision"), "eventtype": row.get("eventtype")}
                    if venue == "ICLR" and year == 2023 and labels:
                        proof["terminology_source"] = "https://iclr.cc/Conferences/2023/AuthorGuide"
                    record(row.get("name") or row.get("title", ""), labels, proof)
                entry["sources"].append(client.used[url])
            except (FetchError, ValueError) as exc:
                entry["limitation"] = str(exc)
            if venue == "CVPR" and year in (2023, 2025):
                url = f"https://cvpr.thecvf.com/Conferences/{year}/AcceptedPapers"
                try:
                    for title, highlight in accepted_highlights(client.get(url)):
                        record(title, ["Highlight"] if highlight else [], {"source": url, "url": url,
                                                                                  "marker": "Highlight"})
                    entry["sources"].append(client.used[url])
                except (FetchError, ValueError) as exc:
                    entry["highlight_limitation"] = str(exc)
            entry["matched_papers"] = len(matched)
            entry["curated_papers"] = sum(r["venue"] == venue and r["year"] == year for r in curated.values())
            coverage.append(entry)
    return {"schema_version": 1, "note": "Positive labels only; an absent badge does not establish poster status. "
            "ICLR 2023 notable-top-5% and notable-top-25% use the official guide's Oral/Spotlight aliases. "
            "Highlight remains distinct. ACL, EMNLP, NAACL, AAAI and KDD are not verified by this collector.",
            "coverage": coverage, "papers": dict(sorted(papers.items()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Rebuild evidence from cached official sources")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--apply-only", action="store_true", help="Reapply committed evidence without HTTP or cache")
    args = parser.parse_args()
    path = ROOT / "data/presentations.json"
    if args.apply_only:
        metadata = json.loads(path.read_text())
    else:
        metadata = collect(ROOT, Client(ROOT / ".cache/proceedings", offline=args.offline, refresh=args.refresh))
        path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    readme = ROOT / "README.md"
    readme.write_text(apply_badges(readme.read_text(), metadata))
    print(json.dumps(dict(Counter(label for r in metadata["papers"].values() for label in r["labels"]))))


if __name__ == "__main__":
    main()
