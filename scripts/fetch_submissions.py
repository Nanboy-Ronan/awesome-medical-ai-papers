#!/usr/bin/env python3
"""Fetch public ICLR submission metadata, with explicit snapshot provenance."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

from paper_index.sources import Client, FetchError, clean

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_REF = "9fcfd1234879a8e5630b5116dde411ec143dd763"


def value(content, name, default=""):
    item = content.get(name, default)
    return item.get("value", default) if isinstance(item, dict) else item


def decision_status(label):
    label = clean(label).casefold()
    if "withdraw" in label:
        return "withdrawn"
    if "desk" in label and "reject" in label:
        return "desk_rejected"
    if label in ("oral", "spotlight", "poster", "accept", "top-25%", "top-5%") or label.startswith("accept ("):
        return "accepted"
    if label in ("reject", "rejected"):
        return "rejected"
    return "unknown"


def normalize_snapshot(rows, year):
    result = {}
    for row in rows:
        identity = str(row.get("id", ""))
        if not identity or not row.get("title"):
            raise ValueError("Snapshot lacks submission ID or title")
        status = decision_status(row.get("status", ""))
        record = {"id": identity, "venue": "ICLR", "year": year,
                  "title": clean(row["title"]), "status": status,
                  "raw_status": row.get("status", ""), "area": row.get("primary_area", row.get("area", "")),
                  "keywords": row.get("keywords", ""), "url": "https://openreview.net/forum?id=" + identity}
        if identity in result and result[identity] != record:
            raise ValueError(f"Conflicting records for {identity}")
        result[identity] = record
    if not any(row["status"] == "rejected" for row in result.values()):
        raise ValueError("No rejected submissions: cannot estimate an acceptance rate")
    return sorted(result.values(), key=lambda r: r["id"])


def fetch_snapshot(client, year):
    url = f"https://raw.githubusercontent.com/papercopilot/paperlists/{SNAPSHOT_REF}/iclr/iclr{year}.json"
    raw = client.get(url)
    if raw.startswith("version https://git-lfs.github.com/spec/v1"):
        expected = dict(line.split(" ", 1) for line in raw.splitlines()[1:])
        url = f"https://media.githubusercontent.com/media/papercopilot/paperlists/{SNAPSHOT_REF}/iclr/iclr{year}.json"
        raw = client.get(url)
        digest = hashlib.sha256(raw.encode()).hexdigest()
        if digest != expected["oid"].split(":", 1)[1]:
            raise ValueError("Git LFS object checksum differs from pinned pointer")
    rows = normalize_snapshot(json.loads(raw), year)
    return rows, {"kind": "third_party_openreview_snapshot", "publisher": "Paper Copilot",
                  "repository": "https://github.com/papercopilot/paperlists", "commit": SNAPSHOT_REF,
                  "url": url, "sha256": hashlib.sha256(raw.encode()).hexdigest(),
                  "limitation": "Historical third-party snapshot, not a live official census. Counts can differ from chair statistics and proceedings."}


def fetch_openreview(client, year):
    if year == 2023:
        raise FetchError("API v1 year requires an explicitly documented import; use the pinned snapshot option")
    api = "https://api2.openreview.net/notes"
    result, expected, seen = [], None, set()
    for offset in range(0, 100000, 1000):
        url = api + "?" + urlencode({"invitation": f"ICLR.cc/{year}/Conference/-/Submission",
                                    "limit": 1000, "offset": offset})
        raw = client.get(url)
        if raw.lstrip().startswith("<"):
            raise FetchError("OpenReview returned a browser verification page, not JSON. No data were accepted.")
        obj = json.loads(raw)
        notes = obj.get("notes", [])
        if expected is None:
            expected = obj.get("count")
        for note in notes:
            if note["id"] in seen:
                raise ValueError("Repeated OpenReview submission during pagination")
            seen.add(note["id"])
            c = note.get("content", {})
            venue_id = value(c, "venueid")
            label = value(c, "venue")
            if venue_id == f"ICLR.cc/{year}/Conference":
                status = "accepted"
            elif venue_id.endswith("/Rejected_Submission"):
                status = "rejected"
            elif venue_id.endswith("/Withdrawn_Submission"):
                status = "withdrawn"
            elif venue_id.endswith("/Desk_Rejected_Submission"):
                status = "desk_rejected"
            else:
                status = "unknown"
            result.append({"id": note["id"], "title": clean(value(c, "title")), "venue": "ICLR", "year": year,
                           "status": status, "raw_status": label, "area": value(c, "primary_area"),
                           "keywords": value(c, "keywords", []), "url": f"https://openreview.net/forum?id={note['id']}"})
        if len(notes) < 1000:
            break
    else:
        raise ValueError("Pagination safety limit reached")
    if expected is not None and len(result) != expected:
        raise ValueError("OpenReview pagination count mismatch")
    if not any(r["status"] == "rejected" for r in result):
        raise ValueError("No public rejected records; acceptance rate is not identifiable")
    return result, {"kind": "official_openreview", "url": api, "expected_count": expected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=("openreview", "snapshot"), required=True)
    parser.add_argument("--years", nargs="+", type=int, choices=(2023, 2024, 2025), default=[2023, 2024, 2025])
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "data/submissions.jsonl")
    parser.add_argument("--manifest", type=Path, default=ROOT / "reports/analysis/submission_sources.json")
    args = parser.parse_args()
    client = Client(ROOT / ".cache/research", offline=args.offline, delay=1, timeout=90)
    all_rows, sources = [], []
    for year in args.years:
        rows, source = (fetch_snapshot if args.source == "snapshot" else fetch_openreview)(client, year)
        counts = dict(Counter(r["status"] for r in rows))
        source.update(venue="ICLR", year=year, count=len(rows), statuses=counts)
        sources.append(source)
        all_rows.extend(rows)
        print(f"ICLR {year}: {len(rows):,} records; {counts}", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in all_rows), encoding="utf-8")
    args.manifest.write_text(json.dumps({"sources": sources, "http_sources": list(client.used.values())}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
