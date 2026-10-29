# Indexing conference proceedings

The indexer enumerates each conference catalog **before** screening papers. It
does not use search-engine results as the candidate universe. The default scope
is the README's 11 conference families and the publication years 2023–2025.

## Run

Python 3.10+ is required. From the repository root:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-index.txt
python scripts/index_papers.py
```

The initial run downloads complete public catalogs and available bulk abstract
exports. Later runs reuse `.cache/proceedings/`. Requests have timeouts, bounded
retries, four workers, and a minimum interval per host. No login or API key is
required. Change `--workers` or `--delay` to reduce load on source websites.

```sh
# A smaller crawl for a particular conference and year.
python scripts/index_papers.py --venues CVPR NeurIPS --years 2025

# Rebuild reports from cached HTTP responses, without network access.
python scripts/index_papers.py --offline

# Apply edited screening rules to the saved full index, without crawling again.
python scripts/index_papers.py --rescreen

# Request missing abstracts for title-matched and broad-review items.
python scripts/index_papers.py --abstracts candidates

# Fetch every accessible missing abstract, including unflagged titles.
# This may require thousands of requests and take much longer.
python scripts/index_papers.py --abstracts all

# Explicitly include Findings, with separate track labels.
python scripts/index_papers.py --include-findings

# Refetch source data instead of using the HTTP cache.
python scripts/index_papers.py --refresh

# Isolate a new run from the default data and reports.
python scripts/index_papers.py --data-dir /tmp/paper-data --report-dir /tmp/paper-reports
```

Use the same venue/year/Findings options with `--offline` as with the original
crawl. `--rescreen` instead preserves the original index scope: venue/year
selection cannot add records to an existing local index. A normal crawl replaces
the output index and reports with the requested scope; it does not append to
earlier runs.

## Sources and track boundaries

| Conferences | Catalog membership | Abstracts |
|---|---|---|
| CVPR, ICCV | CVF all-days proceedings, excluding workshop paths | Exact-title join against official virtual-conference exports |
| ECCV | ECVA proceedings, selected by publication year | Official ECCV virtual-conference export when available |
| NeurIPS | Official proceedings, including Datasets and Benchmarks | Official virtual-conference export |
| ICML | PMLR volumes 202, 235, and 267 | Official virtual-conference export |
| ICLR 2024–2025 | Official ICLR proceedings | Official virtual-conference export |
| ICLR 2023 | Official accepted-presentation export; reported as a fallback | Included in the same export |
| ACL, EMNLP, NAACL | Official ACL Anthology XML, main/long/short volumes | Included in XML |
| AAAI | All archive pages covering the requested years, then all technical and special-track volumes | Individual article metadata with `--abstracts candidates` or `all` |
| KDD | Official Research and Applied Data Science lists; also Datasets and Benchmarks in 2025 | Crossref abstracts for DOI-bearing records with `--abstracts candidates` or `all`, when supplied |

AAAI mixed special-track volumes retain their article section labels, so senior
member presentations and journal-track material can be reviewed separately.
Co-located IAAI/EAAI and student-only volumes are excluded. ACL-family industry,
demo, and workshop tracks are excluded; Findings is opt-in and labeled. This is
an explicit curation boundary, not a claim to index every co-located event.

ICCV 2024, ECCV 2023/2025, and NAACL 2023 are marked `not_held`, rather than
reported as fetch failures or empty successful catalogs. NeurIPS 2025 uses the
explicit `vol38-main-conference` route: the bare year route currently serves
Creative AI. Oral and poster presentations of the same paper are deduplicated.

The proceedings catalog determines membership. Extra titles found only in an
abstract export are **not** automatically added. Joins use normalized full
titles; unmatched titles remain in the index with missing abstracts, and the
report shows join counts. This avoids treating withdrawn, renamed, or extra
presentation records as confirmed proceedings papers.

Official source descriptions: [CVF](https://openaccess.thecvf.com/menu),
[NeurIPS proceedings](https://proceedings.neurips.cc/),
[PMLR](https://proceedings.mlr.press/),
[ICLR proceedings](https://proceedings.iclr.cc/),
[ACL Anthology metadata](https://aclanthology.org/info/development/),
[AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/issue/archive),
[ECVA](https://www.ecva.net/papers.php), and
[KDD](https://www.kdd.org/kdd2025/).

## Outputs

| File | Purpose |
|---|---|
| `data/papers.jsonl` | Every indexed paper, including unflagged and out-of-scope records; title, venue/year/track, available authors/abstracts, official links, and provenance |
| `data/screened.jsonl` | Every paper plus its rule decision, manual decision when present, matching terms, score, topics, and README reconciliation |
| `data/curation.json` | Reviewed inclusion/exclusion decisions, summaries, provenance, DOI verification, and corrections to old entries |
| `reports/candidates.md` | Unlisted candidates and broader review items, grouped by conference/year, with evidence and abstract excerpts |
| `reports/candidates.csv` | The same review queue in a spreadsheet-friendly form |
| `reports/coverage.md` | Human-readable source coverage, counts, limitations, and unmatched/misplaced README entries |
| `reports/coverage.json` | Machine-readable coverage, errors, parameters, rule/README hashes, and source response hashes/timestamps |
| `.cache/proceedings/` | Raw HTTP responses and fetch metadata for reproducibility and offline runs |

Large JSONL files and raw responses are ignored by Git; the scripts, rules,
curation ledger, and review reports can be committed. The indexer writes no
changes to README and does not commit or push anything.

## Screening and review

Edit [`config/medical_topics.json`](../config/medical_topics.json) to extend
medical terms and dataset names. The rules cover medical imaging, pathology,
clinical NLP/EHR, physiological signals, and surgical AI. Short abbreviations
use word boundaries: `CT` must not match the middle of `contrastive`.

- `candidate`: the title matches a specific medical-domain rule.
- `review`: only the abstract matches, or a broad term such as microscopy,
  wearable, or brain appears. General ML methods with medical evaluations stay
  here for scope review.
- `out_of_scope`: the title describes pure biology, such as protein design or
  molecular generation, without an explicit clinical application in the title.
  These records are retained; the rule can be overridden during manual review.
- `not_flagged`: no current rule matched. The record remains available for
  alternative screening, sampling, or a later full-abstract pass.

The score is an explainable ranking heuristic, **not** a relevance probability.
No score cutoff discards flagged papers from the queue. A paper is considered
already listed only after an exact normalized title match. Paper-specific URL
aliases are also checked, but a different title sharing a URL is retained as a
metadata conflict instead of being silently suppressed. Fuzzy matches remain in
the queue as possible duplicates. A shared conference catalog URL never makes
different titles count as duplicates. Exact matches in a
different README year or conference are reported as placement mismatches.

Before adding candidates, confirm the published title and track, read the
abstract, check scope, resolve possible duplicates, and write a concise summary.
KDD records without a supplied DOI need a paper-specific link before inclusion.

## Applying reviewed additions

The current README was expanded from 207 to 1,430 entries using the proceedings
index: 1,226 new papers, 19 corrected existing entries, and 3 entries archived
in the [metadata audit](metadata-audit.md). The ledger records 1,245 approved
records (including correction targets) and 230 exclusions. Broader and
abstract-only candidates still need review; the count is not a recall guarantee.

Only explicit `include` decisions in `data/curation.json` can add papers. A
record contains its stable catalog ID, official title, conference, publication
year, track, sources, and a concise summary. Exclusions have a reason. Existing
exact-title entries are preserved even if they predate the ledger. KDD DOI
overrides retain the accepted-list URL and exact-title/year publisher metadata.
Corrections identify an old entry and an approved replacement; archives retain
the original entry and verification sources. No fuzzy match is auto-merged.

After building the full local index, run:

```sh
# Validate decisions and preview counts without editing.
python scripts/apply_curation.py --check

# Apply approved records and regenerate the metadata audit.
python scripts/apply_curation.py

# Reconcile the updated README and remove known exclusions from the pending queue.
python scripts/index_papers.py --rescreen --offline
```

The applicator validates each approved record against `data/papers.jsonl`,
requires a paper-specific link, preserves the conference → year → topic layout,
and updates the count table. Repeated runs produce the same README. It performs
no network requests, commits, or pushes. New additions need a new explicit review
decision; screening scores alone never approve them.

The indexer loads the ledger by default (`--curation PATH` selects another).
Manual decisions remain separate from rule decisions in the full screened
index. Excluded records leave the pending queue but remain in the index; an
approved unlisted record remains visible even if the rules do not flag it.
Metadata changes invalidate a matching decision and are counted as stale in
coverage output, instead of silently suppressing the record.

## Coverage limits and failure behavior

The index reduces search omissions; keyword rules cannot prove that no relevant
paper is missing. In particular:

- Abstract coverage is reported for every edition. Titles without abstracts are
  searched by title only; `--abstracts all` can reduce that gap where the source
  exposes paper-specific metadata.
- KDD's official accepted-paper lists are identified as such, rather than being
  presented as a publisher-verified proceedings count. Older KDD lists do not
  always provide individual paper links or abstracts.
- An `indexed` catalog means its configured source pages were parsed. An
  independently stated total is checked when the source supplies one; otherwise
  the report explicitly says `no_independent_total`.
- A required catalog/issue failure, count mismatch, pagination loop, or
  suspiciously small result marks the edition `failed` and makes the command
  exit nonzero. Partial data and reports are still written, with that failure
  visible. Missing optional bulk abstracts are warnings, not successful abstract
  coverage.
- Source formats and URLs may change. Extend the relevant parser and regression
  tests when that happens. Refresh the cache to discover source updates.

## Tests

```sh
python -m unittest discover -s tests -v
```

Tests run offline and cover track boundaries, pagination, oral/poster
deduplication, abstract-only matches, biology exclusions, README fuzzy matching,
shared catalog links, URL aliases, and visible failure reports.
