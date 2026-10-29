"""Apply explicit human curation decisions without promoting rule matches."""

from __future__ import annotations

from collections import Counter, defaultdict
import re

from .pipeline import escape, is_paper_url
from .sources import key


TOPICS = (
    "🔬 Medical Imaging & Segmentation",
    "🧫 Computational Pathology & Microscopy",
    "🤖 Foundation Models & Vision-Language",
    "📋 Clinical NLP, EHR & Healthcare",
    "🧠 Neuroimaging, EEG & Brain AI",
    "🫀 Physiological Signals & Medical Time Series",
    "🏥 Surgical AI",
)
GROUPS = (
    ("CVPR", ("CVPR",)), ("NeurIPS", ("NeurIPS",)),
    ("ICML", ("ICML",)), ("ICLR", ("ICLR",)),
    ("ICCV / ECCV", ("ICCV", "ECCV")),
    ("ACL / EMNLP", ("ACL", "EMNLP")), ("NAACL", ("NAACL",)),
    ("AAAI", ("AAAI",)), ("KDD", ("KDD",)),
)


def topic_for(title: str, summary: str = "") -> str:
    text = title + " " + summary
    patterns = (
        (6, r"surg(?:ical|ery)|endoscop|laparoscop|instrument segmentation"),
        (1, r"histopath|computational patholog|whole[- ]slide|\bWSI\b|gigapixel|nucle[ui]|cytolog|mitochond|organoid|microscop|cell (?:topology|track|morph|segment|classif)"),
        (4, r"\bbrain|\bEEG\b|\bfMRI\b|\bMEG\b|electroencephal|neuroimag|neural decod|neural record|intracranial|\bsEEG\b|dementia|alzheimer|parkinson"),
        (5, r"\bECG\b|\bEKG\b|\bPPG\b|sleep|heart[- ]?rate|physiolog|electrocardio|wearable|\brPPG\b"),
        (2, r"vision[- ](?:and[- ])?language|\bVQA\b|visual question|foundation model|\bSAM\b|segment anything|report generation|radiology report|multimodal (?:large )?language"),
        (0, r"segment|tomograph|\bMRI\b|\bCT\b|ultrasound|radiograph|x-ray|medical imag|retin|fundus|reconstruct|registration"),
    )
    for index, pattern in patterns:
        if re.search(pattern, text, re.I):
            return TOPICS[index]
    return TOPICS[3]


def validate_ledger(ledger: dict, index: dict[str, dict]) -> None:
    if ledger.get("schema_version") != 1:
        raise ValueError("Unsupported curation schema")
    for identity, row in ledger["reviewed"].items():
        if identity != row["id"] or row["decision"] not in ("include", "exclude"):
            raise ValueError(f"Invalid review decision: {identity}")
        if row["decision"] == "exclude":
            if not row.get("reason"):
                raise ValueError(f"Missing exclusion reason: {identity}")
            continue
        source = index.get(identity)
        if not source or any(row[field] != source[field] for field in ("venue", "year", "title", "track")):
            raise ValueError(f"Curated metadata differs from catalog: {identity}")
        if not row.get("summary") or not row.get("sources") or not is_paper_url(row["url"]):
            raise ValueError(f"Missing summary, provenance, or paper-specific URL: {identity}")
        if row["url"] not in (source["url"], *source.get("alternate_urls", [])):
            proof = row.get("link_verification", {})
            if (proof.get("url") != row["url"] or proof.get("year") != row["year"]
                    or key(proof.get("publisher_title", "")) != key(row["title"])
                    or proof.get("metadata_source") not in row["sources"]):
                raise ValueError(f"Unverified alternate URL: {identity}")
    for correction in ledger.get("corrections", []):
        if correction["action"] == "replace":
            target = ledger["reviewed"].get(correction["target_id"], {})
            if target.get("decision") != "include":
                raise ValueError("Correction must target an approved record")
        elif correction["action"] != "archive" or not correction.get("original_entry"):
            raise ValueError("Archive must retain the original entry")


def track_suffix(row: dict) -> str:
    # Ordinary technical tracks are implicit; named special tracks stay visible.
    track = row.get("track", "main")
    if track in ("main", "long", "short", "research"):
        return ""
    if track.startswith("AAAI Technical Track on ") and "AI for Social Impact" not in track:
        return ""
    label = {"datasets-and-benchmarks": "Datasets and Benchmarks",
             "applied-data-science": "Applied Data Science"}.get(track, track)
    label = label.replace("AAAI Technical Track on ", "").replace("AAAI Special Track on ", "").removesuffix(" Track")
    return f" *[{escape(label)}]*"


def render_entry(row: dict) -> str:
    return f"- **[{escape(row['title'])}]({row['url']})** — {escape(row['summary'])}{track_suffix(row)}"


def apply_curation(document: str, ledger: dict, index: dict[str, dict]) -> tuple[str, dict]:
    validate_ledger(ledger, index)
    prefix, rest = document.split("## CVPR\n", 1)
    _, suffix = rest.split("## Proceedings indexing\n", 1)
    lookup = {(row["venue"], row["year"], key(row["title"])): row for row in index.values()}
    replacements = {(c["venue"], c["year"], key(c["old_title"])): c for c in ledger.get("corrections", [])}
    entries = {}
    year = venue = None
    existing_topic = TOPICS[0]
    added = corrected = archived = 0
    before_count = 0
    for line in ("## CVPR\n" + rest.split("## Proceedings indexing\n", 1)[0]).splitlines():
        heading = re.fullmatch(r"### (.+) (20\d{2})", line)
        if heading:
            venue, year = heading[1], int(heading[2])
        if line.startswith("#### "):
            existing_topic = next((t for t in TOPICS if line[5:].startswith(t[0])), TOPICS[0])
        entry = re.match(r"- \*\*\[(.+?)\]\((https?://[^\s)]+)\)\*\*(.*)", line)
        if not entry:
            continue
        before_count += 1
        old_key = (venue, year, key(entry[1]))
        correction = replacements.get(old_key)
        if correction and correction["action"] == "archive":
            archived += 1
            continue
        if correction:
            row = ledger["reviewed"][correction["target_id"]]
            rendered = render_entry(row)
            corrected += int(rendered != line)
        else:
            row = lookup.get(old_key)
            if not row:
                raise ValueError(f"Unresolved existing entry: {old_key}")
            # Preserve existing summaries, author credits, and presentation notes.
            url = ledger["reviewed"].get(row["id"], {}).get("url", row["url"])
            if not is_paper_url(url):
                # An existing verified arXiv link is better than a shared catalog.
                url = entry[2]
            description = entry[3]
            raw_label = f" *[{escape(row.get('track', 'main'))}]*"
            if description.endswith(raw_label):
                description = description.removesuffix(raw_label)
            rendered = f"- **[{escape(row['title'])}]({url})**{description}"
            label = track_suffix(row)
            if label and not rendered.endswith(label):
                rendered += label
        if row["id"] in entries:
            raise ValueError(f"Duplicate existing entry: {row['id']}")
        entries[row["id"]] = (row, rendered, existing_topic)
    for identity, row in ledger["reviewed"].items():
        if row["decision"] != "include" or identity in entries:
            continue
        entries[identity] = (row, render_entry(row), topic_for(row["title"], row["summary"]))
        added += 1
    grouped = defaultdict(lambda: defaultdict(list))
    counts = Counter()
    for row, rendered, topic in entries.values():
        grouped[(row["venue"], row["year"])][topic].append((row["title"], rendered))
        counts[(row["venue"], row["year"])] += 1
    table = ["<!-- curated-counts:start -->", f"**{len(entries):,} papers** across 2023–2025. "
             "Entries use official proceedings titles and conference publication years. "
             "See the [curation ledger](data/curation.json), [metadata corrections](docs/metadata-audit.md), "
             "and [remaining review queue](reports/candidates.md).", "",
             "| Conference | 2023 | 2024 | 2025 | Total |", "|---|---:|---:|---:|---:|"]
    for group, venues in GROUPS:
        numbers = [sum(counts[(v, y)] for v in venues) for y in (2023, 2024, 2025)]
        table.append(f"| {group} | " + " | ".join(str(n) for n in numbers) + f" | {sum(numbers)} |")
    table += ["", "Counts describe this curated list, not all relevant papers in each proceedings. "
              "Datasets, benchmarks, and special tracks are labeled when applicable; workshops, "
              "doctoral/student abstracts, and pure molecular/genomics work are outside the current scope.",
              "<!-- curated-counts:end -->", ""]
    prefix = re.sub(r"<!-- curated-counts:start -->.*?<!-- curated-counts:end -->\n\n?", "", prefix, flags=re.S)
    prefix = prefix.replace("## Legend\n", "\n".join(table) + "\n## Legend\n")
    prefix = prefix.replace("| 🧫 | Computational Pathology |", "| 🧫 | Computational Pathology & Microscopy |")
    prefix = prefix.replace("| 📋 | Clinical NLP & EHR |", "| 📋 | Clinical NLP, EHR & Healthcare |")
    lines = [prefix.rstrip(), ""]
    for group, venues in GROUPS:
        lines += [f"## {group}", ""]
        for v, y in sorted((e for e in grouped if e[0] in venues), key=lambda e: (-e[1], venues.index(e[0]))):
            lines += [f"### {v} {y}", ""]
            for topic in TOPICS:
                if topic not in grouped[(v, y)]:
                    continue
                lines += [f"#### {topic}", ""]
                lines += [rendered for _, rendered in sorted(grouped[(v, y)][topic], key=lambda item: key(item[0]))]
                lines.append("")
            lines += ["---", ""]
    lines += ["## Proceedings indexing", "", suffix.lstrip()]
    result = "\n".join(lines).rstrip() + "\n"
    return result, {"before": before_count, "added": added, "corrected": corrected, "archived": archived,
                    "total": len(entries), "approved": sum(r["decision"] == "include" for r in ledger["reviewed"].values())}


def render_audit(ledger: dict) -> str:
    lines = ["# Metadata audit", "", "Reviewed against the 2023–2025 proceedings index. "
             "Corrections retain the original title and link in the machine-readable "
             "[curation ledger](../data/curation.json). Existing exact-title entries also use "
             "paper-specific official links where available.", "", "## Corrections", ""]
    for row in ledger.get("corrections", []):
        if row["action"] != "replace":
            continue
        target = ledger["reviewed"][row["target_id"]]
        lines += [f"- **{row['venue']} {row['year']}**: {escape(row['old_title'])} → "
                  f"[{escape(target['title'])}]({target['url']}). {row['reason']}"]
    lines += ["", "## Entries moved out of the main list", "",
              "These entries remain documented here; an unresolved title is not a claim that no such paper exists.", ""]
    for row in ledger.get("corrections", []):
        if row["action"] != "archive":
            continue
        lines += [f"### {escape(row['old_title'])}", "", row["original_entry"], "", row["reason"], "",
                  "Verification: " + ", ".join(f"[source {i}]({url})" for i, url in enumerate(row["sources"], 1)) + ".", ""]
    return "\n".join(lines).rstrip() + "\n"
