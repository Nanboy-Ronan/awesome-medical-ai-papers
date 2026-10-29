"""Keep retrieval cues separate from reviewed scientific contribution judgments."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from find_science_papers import identity, render_guide, retrieve, score_paper, validate_ledger
from paper_index.pipeline import Rules
from paper_index.sources import Paper

ROOT = Path(__file__).resolve().parents[1]


class ScienceRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / "config/science_retrieval.json").read_text())
        cls.rules = Rules(ROOT / "config/medical_topics.json")
        cls.ledger = json.loads((ROOT / "data/science_review.json").read_text())

    def test_weakly_scored_title_study_is_still_retrieved(self):
        row = Paper("ICML", 2024, "Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data", "https://example.org", abstract="We compare reconstruction training sets.").to_dict()
        self.assertLess(score_paper(row, self.config)[0], self.config["minimum_score"])
        found = retrieve([row], set(), {"papers": []}, self.config, self.rules)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["review_status"], "unreviewed_candidate")
        self.assertNotIn("contribution_tags", found[0])

    def test_repetition_does_not_inflate_score(self):
        row = {"title": "Medical Imaging", "abstract": "shortcut"}
        repeated = {**row, "abstract": "shortcut " * 100}
        self.assertEqual(score_paper(row, self.config), score_paper(repeated, self.config))

    def test_medical_scope_filter_and_reviewed_override(self):
        unrelated = Paper("ICML", 2025, "Rethinking Message Passing for Traffic Networks", "https://example.org").to_dict()
        self.assertEqual(retrieve([unrelated], set(), {"papers": []}, self.config, self.rules), [])
        plain = Paper("ICLR", 2024, "A Plain Title", "https://example.org").to_dict()
        found = retrieve([plain], {identity(plain)}, {"papers": [plain]}, self.config, self.rules)
        self.assertEqual(found[0]["review_status"], "reviewed_for_guide")
        self.assertEqual(found[0]["retrieval_score"], 0)
        with self.assertRaisesRegex(ValueError, "absent from index"):
            retrieve([], set(), {"papers": [plain]}, self.config, self.rules)

    def test_ledger_requires_scope_and_fulltext_provenance(self):
        first_full = next(r for r in self.ledger["papers"] if r["review_level"] == "selected_fulltext_sections")
        for field in ("scope", "pdf_sha256"):
            broken = {**first_full, field: ""}
            with self.assertRaises(ValueError):
                validate_ledger({"papers": [broken]})
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validate_ledger({"papers": [first_full, first_full]})

    def test_committed_guide_matches_reviewed_ledger(self):
        self.assertEqual(render_guide(self.ledger), (ROOT / "reports/science/README.md").read_text())


if __name__ == "__main__":
    unittest.main()
