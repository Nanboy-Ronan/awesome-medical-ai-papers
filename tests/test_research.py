"""Denominator, missing-status, scope, and title-label regression checks."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from fetch_submissions import decision_status, normalize_snapshot
from paper_index.research import TopicRules, acceptance_analysis, aggregate_shares, analyse, eligible, wilson
from paper_index.sources import Paper, key

ROOT = Path(__file__).resolve().parents[1]


class Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = TopicRules(json.loads((ROOT / "config/research_topics.json").read_text()))

    def test_mixed_track_denominator_matches_research_scope(self):
        papers = [Paper("AAAI", 2025, "Medical Imaging", "x", "AAAI Technical Track on Computer Vision I").to_dict(),
                  Paper("AAAI", 2025, "Clinical Abstract", "y", "AAAI Doctoral Consortium Track").to_dict(),
                  Paper("AAAI", 2025, "Generic Research", "z", "AAAI Technical Track on Machine Learning I").to_dict()]
        rows = aggregate_shares(papers, {("AAAI",2025,key("Medical Imaging"))})
        self.assertEqual(rows[0]["catalog_records"], 3)
        self.assertEqual(rows[0]["eligible_research_records"], 2)
        self.assertEqual(rows[0]["curated_share_of_eligible_pct"], 50)
        self.assertFalse(eligible(papers[1]))
        self.assertEqual(len(rows), 1)  # Missing editions are not zero-percent rows.

    def test_unknown_and_withdrawn_are_not_rejections(self):
        self.assertEqual(decision_status("Withdrawn after acceptance"), "withdrawn")
        self.assertEqual(decision_status("Desk Reject"), "desk_rejected")
        self.assertEqual(decision_status("Pending"), "unknown")
        self.assertEqual(decision_status("Top-5%"), "accepted")
        with self.assertRaisesRegex(ValueError, "No rejected"):
            normalize_snapshot([{"id":"a", "title":"Medical AI", "status":"Poster"}], 2025)

    def test_rates_condition_on_explicit_final_decisions(self):
        rows = [{"id":str(i),"venue":"ICLR","year":2025,"title":title,"status":status,"url":"https://openreview.net/forum?id="+str(i)}
                for i,(title,status) in enumerate([
                    ("Medical Imaging", "accepted"), ("Clinical Prediction", "rejected"),
                    ("Clinical Withdrawn", "withdrawn"), ("Medical Desk Rejection", "desk_rejected"),
                    ("Clinical Pending", "unknown"), ("General Optimization", "accepted")])]
        rates, _, _, _ = acceptance_analysis(rows, [], self.rules)
        med = next(r for r in rates if r["group"]=="medical_keyword" and r["definition"]=="specific_title_proxy")
        self.assertEqual(med["decision_rate_pct"], 50)
        self.assertEqual(med["decision_denominator"], 2)
        self.assertEqual(med["accepted_fraction_observed_pool_pct"], 20)
        self.assertEqual(med["unknown"], 1)

    def test_submission_identity_conflicts_stop_analysis(self):
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            normalize_snapshot([{"id":"a","title":"A","status":"Poster"}, {"id":"a","title":"B","status":"Reject"}],2025)

    def test_false_friends_and_keyword_document_frequency(self):
        self.assertFalse(self.rules.medical_proxy("Clinical-style industrial bearing fault diagnosis"))
        self.assertFalse(self.rules.medical_proxy("An EEGless Network for General Optimization"))
        self.assertTrue(self.rules.medical_proxy("Self-supervised EEG decoding"))
        words = self.rules.keywords("Diffusion diffusion diffusion and foundation models")
        self.assertIn("diffusion", words)
        self.assertIn("foundation models", words)
        self.assertEqual(sum(w=="diffusion" for w in words),1)

    def test_abstract_does_not_silently_change_title_topic_counts(self):
        p = Paper("CVPR",2025,"A Generic Title","https://x/html/paper",abstract="Clinical medical imaging using diffusion models.").to_dict()
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"README.md"
            path.write_text("### CVPR 2025\n- **[A Generic Title](https://x/html/paper)** — Summary.\n")
            result=analyse([p],path,self.rules)
            self.assertEqual(result["annotated"][0]["domains"],"")
            self.assertEqual(result["annotated"][0]["methods"],"")
            self.assertTrue(result["annotated"][0]["abstract_available"])
            with self.assertRaisesRegex(ValueError,"cannot be aligned"):
                analyse([],path,self.rules)

    def test_wilson_boundaries_and_known_interval(self):
        self.assertEqual(wilson(0,0),(None,None))
        low, high=wilson(50,100)
        self.assertAlmostEqual(low,40.383,places=2)
        self.assertAlmostEqual(high,59.617,places=2)
        self.assertAlmostEqual(wilson(0,10)[0],0,places=8)
        self.assertAlmostEqual(wilson(10,10)[1],100,places=8)


if __name__=="__main__":
    unittest.main()
