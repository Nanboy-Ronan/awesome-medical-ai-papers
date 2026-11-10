# Presentation labels

The README and searchable catalog display **[Oral]**, **[Spotlight]**, and
**[Highlight]** badges verified against official conference records. The catalog
also provides a presentation filter and accepts these labels as search terms.

The committed [presentation evidence](../data/presentations.json) records each
labeled paper's conference, publication year, title, labels, source URL, and raw
decision/event type or program marker. Source checksums and retrieval dates are
recorded per edition. Matching requires the same venue, year, and normalized
title; repeated oral/poster events produce one paper with combined evidence.
Presentation metadata never adds papers to the curated corpus.

## Coverage

| Conference | Editions checked | Evidence |
|---|---|---|
| CVPR | 2023–2025 | Official virtual exports; accepted-paper Highlight markers for 2023 and 2025 |
| NeurIPS | 2023–2025 | Official virtual export decisions and event types |
| ICML | 2023–2025 | Official virtual export decisions and event types |
| ICLR | 2023–2025 | Official virtual export decisions and event types |
| ICCV | 2023, 2025 | 2023 main conference program; 2025 official virtual export |
| ECCV | 2024 | Official virtual export event types |
| ACL, EMNLP, NAACL, AAAI, KDD | Pending | No presentation labels asserted |

These sources match 894 of the 895 curated papers in the checked conference
editions. The unmatched ICCV 2025 title is “Cracking Instance Jigsaw Puzzles:
An Alternative to Multiple Instance Learning for Whole Slide Image Analysis”;
the virtual export uses a different title. It remains unclassified rather than
being joined through fuzzy title similarity.

An absent badge **does not establish poster status**. Coverage of presentation
tiers depends on the source: for example, CVPR 2023's export contains only poster
events and does not identify its award-candidate plenary talks. Its verified
Highlight markers are retained under their official name. Highlight is not
renamed Spotlight, and awards alone are not treated as oral evidence.

Spotlights often appear as `eventtype=Poster`; the collector therefore checks
the decision too. ICML 2023's `Accept (Oral & Poster)` becomes Oral. For ICLR
2023, `notable-top-5%` becomes Oral and `notable-top-25%` becomes Spotlight,
following the terminology explicitly explained in the
[official author guide](https://iclr.cc/Conferences/2023/AuthorGuide).

## Reproduce

```sh
# Retrieve official sources, save evidence, and update README badges.
python scripts/label_presentations.py

# Rebuild from the existing verified HTTP cache.
python scripts/label_presentations.py --offline

# Reapply committed evidence, without network access or a local cache.
python scripts/label_presentations.py --apply-only

# Include badges and filters in the generated website.
python scripts/build_site.py
```

`scripts/apply_curation.py` reapplies committed presentation evidence after
curating entries, so corrections and regenerated entries retain verified badges.
The website consumes the same evidence directly. Source-refresh failures and
edition-level match counts are recorded in `coverage` in the evidence file;
review that section before publishing refreshed labels.
