# Medical AI conference research, 2023–2025

Three reproducible analyses of the curated awesome list and its full proceedings
index. **Shares of published papers and submission acceptance rates have different
denominators.** The accepted-paper analysis covers all indexed conference editions;
the decision-rate comparison is restricted to ICLR public snapshots.

1. [Medical share of proceedings by conference and year](medical-share.md)
2. [Medical versus other-title acceptance rates, with source and denominator limits](acceptance-rates.md)
3. [Yearly research domains, methods, and title keywords](topics.md)

| Year | Curated medical | Eligible indexed papers | Observed medical share |
|---|---|---|---|
| 2023 | 282 | 15799 | 1.78% |
| 2024 | 443 | 20315 | 2.18% |
| 2025 | 705 | 26607 | 2.65% |

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
