"""Checks for unsafe metadata promotion, duplicate aliases, and stable updates."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from paper_index.curation import apply_curation, validate_ledger
from paper_index.pipeline import Rules, write_reports
from paper_index.sources import Client, Paper


class Curation(unittest.TestCase):
    def setUp(self):
        self.paper = Paper("CVPR", 2025, "Medical Segmentation", "https://example.org/html/paper.html", sources=["https://example.org/catalog"])
        self.row = {**self.paper.to_dict(), "decision": "include", "summary": "Segments medical images."}
        self.index = {self.paper.identity: self.paper.to_dict()}
        self.ledger = {"schema_version": 1, "reviewed": {self.paper.identity: self.row}, "corrections": []}
        self.document = "# List\n\n## Legend\n\n## CVPR\n\n## Proceedings indexing\n\nInstructions.\n"

    def test_alias_correction_is_not_a_second_paper_and_run_is_stable(self):
        self.ledger["corrections"] = [{"action": "replace", "venue": "CVPR", "year": 2025,
                                      "old_title": "Old Incorrect Title", "target_id": self.paper.identity}]
        source = self.document.replace("## CVPR\n", "## CVPR\n\n### CVPR 2025\n\n- **[Old Incorrect Title](https://example.org/old)** — Incorrect summary.\n")
        result, stats = apply_curation(source, self.ledger, self.index)
        self.assertEqual((stats["added"], stats["corrected"], stats["total"]), (0, 1, 1))
        self.assertNotIn("Incorrect summary", result)
        again, stats = apply_curation(result, self.ledger, self.index)
        self.assertEqual(result, again)
        self.assertEqual(stats["added"], 0)

    def test_missing_catalog_member_or_changed_title_cannot_be_added(self):
        with self.assertRaisesRegex(ValueError, "differs from catalog"):
            validate_ledger(self.ledger, {})
        self.row["title"] = "Unverified Replacement"
        with self.assertRaisesRegex(ValueError, "differs from catalog"):
            validate_ledger(self.ledger, self.index)

    def test_catalog_url_and_unverified_doi_are_rejected(self):
        self.row["url"] = "https://example.org/catalog"
        with self.assertRaisesRegex(ValueError, "paper-specific"):
            validate_ledger(self.ledger, self.index)
        self.row["url"] = "https://doi.org/10.1145/123.456"
        with self.assertRaisesRegex(ValueError, "Unverified alternate"):
            validate_ledger(self.ledger, self.index)
        self.row["sources"].append("https://api.crossref.org/works/10.1145/123.456")
        self.row["link_verification"] = {"url": self.row["url"], "publisher_title": self.row["title"],
                                         "year": 2025, "metadata_source": self.row["sources"][-1]}
        validate_ledger(self.ledger, self.index)

    def test_existing_summary_survives_and_publication_year_is_retained(self):
        source = self.document.replace("## CVPR\n", "## CVPR\n\n### CVPR 2025\n\n- **[Medical Segmentation](https://arxiv.org/abs/2312.00001)** — Original description. *Author*\n")
        result, stats = apply_curation(source, self.ledger, self.index)
        self.assertIn("Original description. *Author*", result)
        self.assertIn("### CVPR 2025", result)
        self.assertEqual(stats["added"], 0)
        self.assertIn(self.paper.url, result)

    def test_excluded_record_is_retained_in_index_but_not_pending_queue(self):
        self.row.update(decision="exclude", reason="Outside scope.")
        rules = Rules(Path(__file__).resolve().parents[1] / "config/medical_topics.json")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text(self.document)
            report = write_reports([self.paper], [], rules, readme, root / "data", root / "reports",
                                   Client(root / "cache", offline=True), [], {}, self.ledger)
            self.assertEqual(report["candidate_count"], 0)
            row = json.loads((root / "data/screened.jsonl").read_text())
            self.assertEqual(row["manual_decision"], "exclude")
            self.assertEqual(row["decision"], "candidate")
            # A changed metadata record must be reviewed again, not suppressed.
            self.row["track"] = "stale track"
            report = write_reports([self.paper], [], rules, readme, root / "data", root / "reports",
                                   Client(root / "cache", offline=True), [], {}, self.ledger)
            self.assertEqual(report["candidate_count"], 1)
            self.assertEqual(report["stale_curations"], [self.paper.identity])


if __name__ == "__main__":
    unittest.main()
