"""Keep the README taxonomy figure in step with the curated topic sections."""

from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from build_taxonomy import CATEGORIES, OUTPUT, render, topic_counts


class Taxonomy(unittest.TestCase):
    def setUp(self):
        self.readme=(ROOT/"README.md").read_text()

    def test_committed_figure_matches_readme(self):
        self.assertEqual(OUTPUT.read_text(),render(topic_counts(self.readme)),"Rerun scripts/build_taxonomy.py")

    def test_figure_is_valid_and_embedded(self):
        ET.fromstring(OUTPUT.read_text())
        self.assertIn('src="assets/medical-ai-papers-taxonomy.svg"',self.readme)
        self.assertIn("- [Taxonomy](#taxonomy)",self.readme)

    def test_counts_cover_every_topic(self):
        counts=topic_counts(self.readme)
        self.assertEqual(set(counts),{category[0] for category in CATEGORIES})
        stated=re.search(r"\*\*([\d,]+) papers\*\* across",self.readme)[1]
        self.assertEqual(sum(counts.values()),int(stated.replace(",","")))

    def test_unknown_topic_is_rejected(self):
        with self.assertRaises(ValueError):
            render({"🧪":1})


if __name__=="__main__":
    unittest.main()
