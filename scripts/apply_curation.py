#!/usr/bin/env python3
"""Apply reviewed records to README; no HTTP, commits, or automatic approvals."""

import argparse
import json
from pathlib import Path

from paper_index.curation import apply_curation, render_audit


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--ledger", type=Path, default=ROOT / "data/curation.json")
    parser.add_argument("--index", type=Path, default=ROOT / "data/papers.jsonl")
    parser.add_argument("--audit", type=Path, default=ROOT / "docs/metadata-audit.md")
    parser.add_argument("--check", action="store_true", help="Validate and show counts without writing files")
    args = parser.parse_args()
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    index = {}
    with args.index.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            index[row["id"]] = row
    result, stats = apply_curation(args.readme.read_text(encoding="utf-8"), ledger, index)
    print(json.dumps(stats, indent=2))
    if not args.check:
        args.readme.write_text(result, encoding="utf-8")
        args.audit.write_text(render_audit(ledger), encoding="utf-8")


if __name__ == "__main__":
    main()
