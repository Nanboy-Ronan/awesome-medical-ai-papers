"""Presentation decisions, provenance, and badges must agree across outputs."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from paper_index.presentations import accepted_highlights, apply_badges, iccv_program, identity, virtual_labels
from paper_index.pipeline import read_readme
from build_site import Site

ROOT = Path(__file__).resolve().parents[1]


class Presentations(unittest.TestCase):
    def test_decision_takes_account_of_spotlight_posters(self):
        self.assertEqual(virtual_labels({"eventtype": "Poster", "decision": "Accept (spotlight poster)"}, "ICML", 2025), ["Spotlight"])
        self.assertEqual(virtual_labels({"eventtype": "Poster", "decision": "Accept (Oral & Poster)"}, "ICML", 2023), ["Oral"])
        self.assertEqual(virtual_labels({"eventtype": "Oral", "decision": None}, "ECCV", 2024), ["Oral"])
        self.assertEqual(virtual_labels({"eventtype": "Poster", "decision": "Accept: Poster (Highlight)"}, "CVPR", 2024), ["Highlight"])
        self.assertEqual(virtual_labels({"eventtype": "Poster", "decision": "Accept (Outstanding Paper)"}, "NeurIPS", 2023), [])

    def test_iclr_alias_is_specific_to_2023(self):
        for decision, label in (("notable-top-5%", "Oral"), ("notable-top-25%", "Spotlight")):
            row = {"eventtype": "Poster", "decision": "Accept: " + decision}
            self.assertEqual(virtual_labels(row, "ICLR", 2023), [label])
            self.assertEqual(virtual_labels(row, "ICLR", 2024), [])

    def test_html_sources_do_not_confuse_authors_or_project_titles(self):
        self.assertEqual(accepted_highlights('<table><tr><td><strong>Clinical Model</strong><a>Oral project</a><img title="Highlight"><i>Author</i></td></tr></table>'), [("Clinical Model", True)])
        html = '<table class="Orals"><tr><td>Time</td><td>Session</td><td>Clinical Model<br><em>Author</em><br><small>Paper ID:1</small></td></tr></table>'
        self.assertEqual(iccv_program(html), [("Clinical Model", ["Oral"])])

    def test_badges_are_idempotent_and_preserve_summaries(self):
        document = '### ICML 2025\n- **[Clinical Model](https://example.org/paper)** — Summary. *[Special Track]*\n'
        metadata = {"papers": {"ICML:2025:clinicalmodel": {"labels": ["Oral", "Highlight"]}}}
        result = apply_badges(document, metadata)
        self.assertIn('**[Oral]** **[Highlight]** — Summary. *[Special Track]*', result)
        self.assertEqual(apply_badges(result, metadata), result)
        self.assertEqual(apply_badges(result, {"papers": {}}), document)

    def test_committed_evidence_matches_readme_and_site(self):
        metadata = json.loads((ROOT / "data/presentations.json").read_text())
        document = (ROOT / "README.md").read_text()
        self.assertEqual(apply_badges(document, metadata), document)
        curated = {identity(row) for row in read_readme(ROOT / "README.md")}
        self.assertTrue(set(metadata["papers"]) <= curated)
        site = Site()
        for row in site.rows:
            proof = metadata["papers"].get(identity(row), {})
            self.assertEqual(row["presentations"], proof.get("labels", []))
            if row["presentations"]:
                self.assertTrue(proof["evidence"])
                self.assertIn('class="presentation"', site.cards([row]))


if __name__ == "__main__":
    unittest.main()
