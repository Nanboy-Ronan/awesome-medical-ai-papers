#!/usr/bin/env python3
"""Build complete conference catalogs, then screen and reconcile with README."""

from __future__ import annotations

import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import sys

from paper_index.sources import Client, Indexer, Paper, VENUES, YEARS, deduplicate
from paper_index.pipeline import Rules, enrich_missing, write_reports


ROOT = Path(__file__).resolve().parents[1]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", nargs="+", type=int, choices=YEARS, default=list(YEARS))
    parser.add_argument("--venues", nargs="+", choices=VENUES, default=list(VENUES))
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--rules", type=Path, default=ROOT / "config/medical_topics.json")
    parser.add_argument("--curation", type=Path, default=ROOT / "data/curation.json",
                        help="Manual review ledger; known exclusions leave the pending queue")
    parser.add_argument("--cache-dir", type=Path, default=ROOT / ".cache/proceedings")
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data")
    parser.add_argument("--report-dir", type=Path, default=ROOT / "reports")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--delay", type=float, default=0.5, help="Minimum seconds between requests per host")
    parser.add_argument("--offline", action="store_true", help="Use cached responses only; missing responses remain failures")
    parser.add_argument("--refresh", action="store_true", help="Refetch HTTP data instead of using cache")
    parser.add_argument("--include-findings", action="store_true", help="Include separately labeled ACL/EMNLP/NAACL Findings")
    parser.add_argument("--abstracts", choices=("none", "candidates", "all"), default="none",
                        help="Extra per-paper abstract fetches; bulk abstracts are always used. 'all' can require many thousands of requests")
    parser.add_argument("--rescreen", action="store_true", help="Reuse existing data/papers.jsonl, skipping catalog crawling; cannot expand its coverage")
    args = parser.parse_args(argv)
    if args.workers < 1 or args.delay < 0:
        parser.error("--workers must be positive and --delay must be nonnegative")
    if args.offline and args.refresh:
        parser.error("--offline and --refresh cannot be combined")
    client = Client(args.cache_dir, offline=args.offline, refresh=args.refresh, delay=args.delay)
    rules = Rules(args.rules)
    curation = json.loads(args.curation.read_text(encoding="utf-8")) if args.curation.exists() else None
    papers = []
    coverage = []
    if args.rescreen:
        # Retain the original crawl coverage and source provenance.
        prior = json.loads((args.report_dir / "coverage.json").read_text(encoding="utf-8"))
        coverage = prior["coverage"]
        for row in prior.get("http_sources", []):
            client.used[row["url"]] = row
        for line in (args.data_dir / "papers.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            row.pop("id", None)
            papers.append(Paper(**row))
    else:
        indexer = Indexer(client, include_findings=args.include_findings)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            jobs = {pool.submit(indexer.index, v, y): (v, y) for v in dict.fromkeys(args.venues) for y in sorted(set(args.years))}
            for future in as_completed(jobs):
                venue, year = jobs[future]
                try:
                    rows, status = future.result()
                except Exception as exc:
                    rows, status = [], {"venue": venue, "year": year, "status": "failed", "sources": [], "notes": [], "error": str(exc)}
                papers.extend(rows)
                coverage.append(status)
                print(f"{venue} {year}: {status['status']}, {len(rows):,} papers, "
                      f"{sum(bool(p.abstract) for p in rows):,} abstracts" + (f" — {status['error']}" if status.get("error") else ""), flush=True)
    papers = deduplicate(papers)
    failures = enrich_missing(papers, rules, client, args.abstracts, args.workers)
    coverage.sort(key=lambda e: (VENUES.index(e["venue"]), e["year"]))
    options = {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()}
    # Paths in the report stay portable across checkouts.
    for field in ("readme", "rules", "curation", "cache_dir", "data_dir", "report_dir"):
        try:
            options[field] = str(Path(options[field]).relative_to(ROOT))
        except ValueError:
            pass
    if curation is not None:
        options["curation_sha256"] = hashlib.sha256(args.curation.read_bytes()).hexdigest()
    if args.rescreen:
        original_options = prior.get("options", {})
        while "original_index_options" in original_options:
            original_options = original_options["original_index_options"]
        options["original_index_options"] = original_options
        failures = prior.get("abstract_fetch_failures", []) + failures
    report = write_reports(papers, coverage, rules, args.readme, args.data_dir, args.report_dir, client, failures, options, curation)
    print(f"Indexed {report['paper_count']:,} unique papers; {report['abstract_count']:,} abstracts; "
          f"{report['candidate_count']:,} unlisted screening items; {report['failed_editions']} failed editions.")
    print(f"Coverage: {args.report_dir / 'coverage.md'}\nCandidates: {args.report_dir / 'candidates.md'}")
    # Reports are useful even after a failure; automation must still see failure.
    return 1 if report["failed_editions"] else 0


if __name__ == "__main__":
    sys.exit(main())
