# Research methodology

This repository studies three different questions. Their denominators are not
interchangeable.

| Question | Numerator | Denominator | Interpretation |
|---|---|---|---|
| How much of a conference's published output is medical AI? | Curated medical papers in an edition | Indexed eligible research records in the same edition | Observed lower-bound share of this indexed corpus |
| Are medical submissions accepted more often? | Accepted submissions matching a medical title rule | Accepted + rejected submissions matching the same rule | Conditional decision rate in a public ICLR snapshot |
| What topics are medical papers studying? | Curated papers matching a domain/method/keyword | All curated medical papers in the same publication year | Multi-label title prevalence |

## Corpus and track alignment

The accepted-paper corpus joins README titles to `data/papers.jsonl` using
conference, publication year, and the indexer's normalized exact title key.
Any unmatched entry or duplicate identity stops the analysis. Curated records
are not promoted from keyword candidates. The local index retains every parsed
record, including broad and nonmedical records.

Both raw catalog and research-only denominators are exported. Mixed AAAI
volumes contain formats that should not be pooled with full research papers;
the research-only predicate is explicit in `paper_index/research.py`. NeurIPS
Datasets and Benchmarks and KDD research/applied-data-science/datasets tracks
remain in combined-track proceedings shares, with separate track tables.
Chair-reported main-track acceptance counts are never substituted into those
combined-track denominators. ICLR 2023 uses the accepted-presentation fallback
documented by the indexer. Catalog counts can differ from later chair statistics.

Missing editions are absent rather than zero. Pooled yearly shares have a
changing venue composition. An equal-weight sensitivity analysis uses only
families present in every year and combines alternating ICCV/ECCV. Neither
approach corrects curation incompleteness or domain-label errors. Broad
unreviewed candidates make the curated medical numerator a lower bound, not
an exhaustive domain census. The remaining accepted records are not asserted
to be nonmedical.

## Submission outcomes and comparison groups

OpenReview's [official retrieval documentation](https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-all-notes-for-submissions-reviews-rebuttals-etc)
distinguishes accepted, rejected, withdrawn, and desk-rejected notes. Official
note queries returned a browser-verification page in this environment. The
fetcher rejects that HTML; it never treats it as an empty successful dataset.

The completed comparison uses the dataset publisher's
[Paper Copilot snapshots](https://github.com/papercopilot/paperlists), pinned to
commit `9fcfd1234879a8e5630b5116dde411ec143dd763`. This is a third-party archival
dataset, not a live official census. The original snapshots remain in the local
HTTP cache. Source URLs, response hashes, and Git LFS object verification are
recorded; only derived labels and aggregate statistics are committed. The source
data's rights remain with their respective providers.

Submissions are deduplicated by OpenReview ID. Explicit status mapping preserves
withdrawals, desk rejections, and unknowns. `Top-5%` and `Top-25%` are accepted
presentation tiers in the 2023 snapshot, validated against accepted titles.
Unknown or absent decisions never become implicit rejections.

The headline comparison uses exactly the same medical keyword rule for accepted
and rejected titles, without using the accepted-only curated labels to classify
one side. It compares medical-keyword titles with other titles, not verified
medical/nonmedical ground truth. A broader rule is a sensitivity definition,
not an improvement with established accuracy. The full rules are in
[`config/research_topics.json`](../config/research_topics.json).

Primary rate: `accepted / (accepted + rejected)` within year and title group.
Withdrawn, desk-rejected, and unknown records are excluded from that denominator
and exported separately. A sensitivity column is `accepted / observed pool`,
which includes those other statuses but is still not guaranteed to reproduce
the conference's official submission denominator. Chair statistics and snapshot
statistics remain separate, including their disagreements.

Wilson 95% intervals describe binomial variability conditional on this grouping.
They do not correct label error, missingness, snapshot selection, review-policy
changes, or dependence among submissions. These records are observational, not
randomly assigned experiments. Differences cannot establish that a conference
prefers or penalizes medical research. Small groups have substantial uncertainty.

The 2024/2025 self-reported area labels are exported separately; changing taxonomies
and absent 2023 areas prohibit a clean longitudinal comparison of every named
field. Conferences without a complete public rejected-submission pool receive
no fabricated domain acceptance estimate.

## Topics and keywords

All quantitative labels use titles, even when abstracts exist. This keeps text
availability consistent across years and avoids attributing improved abstract
coverage to a new topic trend. Domains and methods form separate multi-label
families. A paper may count in several rows; row percentages do not sum to 100%.
Zero matches mean no matching titles, not absence of research on the topic.

Keywords are deterministic title unigrams and adjacent bigrams. The configuration
publishes token stopwords and phrase exceptions. Each term counts at most once
per paper. We export document counts and normalized yearly prevalence, with
explicit minimum-frequency filters for keyword changes. No learned model, LLM
labeling, or causal trend attribution is used in the quantitative pipeline.
The title-topic assignments make no model calls. Corpus membership comes from
the repository's recorded curation decisions, including assistant-aided review;
these are not independently validated expert subject labels. Input and
configuration hashes appear in `reports/analysis/summary.json`.

## Reproduce and inspect

```sh
python -m pip install -r requirements-analysis.txt
python scripts/index_papers.py --abstracts candidates
python scripts/fetch_submissions.py --source snapshot
python scripts/analyze_research.py
python -m unittest discover -s tests -v
```

After the first download, use `--offline` for the indexer/fetcher. The analysis
makes no HTTP requests. Use `--source openreview --years 2024 2025` to attempt
official API v2 acquisition instead; failure is explicit and leaves existing
inputs untouched. A missing submission input stops the combined analysis rather
than generating an accepted-only pseudo-acceptance rate.

Study scope is 2023–2025, not the current year's incomplete conference cycle.
Outputs describe publication records, not unique projects or clinical utility.
