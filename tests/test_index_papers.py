"""Offline regression tests for omission-prone source formats and screening."""

from pathlib import Path
import json
import hashlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from paper_index.sources import (Client, FetchError, Indexer, Paper, deduplicate, edition_exists,
                                parse_acl, parse_aaai_archive, parse_aaai_issue, parse_cvf,
                                parse_kdd, parse_neural, parse_pmlr, parse_virtual, supplement)
from paper_index.pipeline import Rules, canonical_url, parse_abstract, reconcile, write_reports

ROOT = Path(__file__).resolve().parents[1]


class Parsers(unittest.TestCase):
    def test_cvf_main_membership_and_relative_links(self):
        page = '''<dt class="ptitle"><a href="/content/CVPR2025/html/A_paper.html">Medical &amp; AI</a></dt>
                  <dt class="ptitle"><a href="/content/CVPR2025W/html/B.html">Workshop</a></dt>'''
        papers = parse_cvf(page, "https://openaccess.thecvf.com/CVPR2025?day=all", "CVPR", 2025)
        self.assertEqual([p.title for p in papers], ["Medical & AI"])
        self.assertTrue(papers[0].url.startswith("https://openaccess.thecvf.com/content/"))

    def test_neurips_declared_count_and_track(self):
        page = '''<h3>2 papers</h3><ul class="paper-list">
        <li><a href="/paper_files/paper/2025/hash/a-Abstract-Conference.html">Medical Imaging</a></li>
        <li><a href="/paper_files/paper/2025/hash/b-Abstract-Datasets_and_Benchmarks_Track.html">Clinical Benchmark</a></li></ul>'''
        rows, count = parse_neural(page, "https://proceedings.neurips.cc/", "NeurIPS", 2025)
        self.assertEqual(count, len(rows))
        self.assertEqual(rows[1].track, "datasets-and-benchmarks")

    def test_virtual_oral_poster_duplicates_and_pagination(self):
        row = {"name": "Clinical Model", "eventtype": "Poster", "authors": [], "abstract": "Example abstract", "paper_url": "https://openreview.net/forum?id=a"}
        data = {"count": 2, "next": None, "results": [row, {**row, "eventtype": "Oral"}]}
        rows, raw_count = parse_virtual(json.dumps(data), "https://iclr.cc/export", "ICLR", 2023)
        self.assertEqual(len(rows), 1)
        self.assertEqual(raw_count, 2)
        with self.assertRaises(FetchError):
            parse_virtual(json.dumps({**data, "next": "page2"}), "url", "ICLR", 2023)

    def test_pmlr_catalog(self):
        html = '<div class="paper"><p class="title">ECG Model</p><span class="authors">A, B</span><a href="x25.html">abs</a><a href="x.pdf">pdf</a></div>'
        rows = parse_pmlr(html, "https://proceedings.mlr.press/v267/", 2025)
        self.assertEqual(rows[0].url, "https://proceedings.mlr.press/v267/x25.html")
        self.assertEqual(rows[0].authors, ["A", "B"])

    def test_acl_main_short_long_included_workshop_excluded(self):
        xml = '''<collection id="2025.acl"><volume id="long"><paper id="1"><title>Clinical <fixed-case>NLP</fixed-case></title><author><first>A</first><last>B</last></author><abstract>Medical data.</abstract></paper></volume>
        <volume id="short"><paper id="2"><title>EHR</title></paper></volume>
        <volume id="industry"><paper id="3"><title>Other track</title></paper></volume></collection>'''
        rows = parse_acl(xml, "source", "ACL", 2025)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].title, "Clinical NLP")
        self.assertEqual(rows[0].authors, ["A B"])
        self.assertEqual(rows[1].url, "https://aclanthology.org/2025.acl-short.2/")

    def test_aaai_pagination_and_mixed_sections(self):
        page = '<a class="title" href="/issue/view/1">AAAI-25 Technical Tracks 1</a><a class="next" href="/issue/archive/2">Next</a>'
        rows, next_url = parse_aaai_archive(page, "https://example.org/issue/archive")
        self.assertEqual(rows[0][0], 2025)
        self.assertEqual(next_url, "https://example.org/issue/archive/2")
        issue = '<div class="section"><h2>AAAI Special Track</h2><div class="obj_article_summary"><h3 class="title"><a href="/article/view/1">Medical Paper</a></h3><div class="authors">A, B</div></div></div>'
        papers = parse_aaai_issue(issue, "https://example.org/issue/1", 2025)
        self.assertEqual(papers[0].track, "AAAI Special Track")

    def test_kdd_multiple_tables_and_nested_strong(self):
        page = '<table><td><strong>Medical Benchmark<strong></strong></strong><br>DOI: 10.1145/123.456</td></table><table><td><strong>Clinical Data Model</strong></td></table>'
        rows = parse_kdd(page, "https://kdd.org/list", 2025, "research")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].url, "https://doi.org/10.1145/123.456")
        self.assertEqual(rows[1].url, "https://kdd.org/list")

    def test_supplement_does_not_introduce_nonmembers(self):
        rows = [Paper("ICML", 2025, "Medical Model", "https://publisher/paper")]
        other = [Paper("ICML", 2025, "Medical Model!", "https://openreview/a", abstract="a", abstract_source="bulk"),
                 Paper("ICML", 2025, "Withdrawn Model", "https://openreview/b")]
        self.assertEqual(supplement(rows, other), 1)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].abstract, "a")

    def test_missing_editions(self):
        self.assertFalse(edition_exists("ICCV", 2024))
        self.assertFalse(edition_exists("ECCV", 2025))
        self.assertFalse(edition_exists("NAACL", 2023))
        self.assertTrue(edition_exists("CVPR", 2023))

    def test_declared_total_mismatch_fails_edition(self):
        page = '<h3>101 papers</h3><ul class="paper-list">' + ''.join(
            f'<li><a href="/paper_files/paper/2025/hash/{n}-Abstract-Conference.html">Paper {n}</a></li>'
            for n in range(100)) + '</ul>'
        class FakeClient:
            def get(self, url):
                return page
        papers, coverage = Indexer(FakeClient()).index("NeurIPS", 2025)
        self.assertEqual(len(papers), 100)
        self.assertEqual(coverage["status"], "failed")
        self.assertIn("101", coverage["error"])

    def test_aaai_missing_volume_fails_edition(self):
        indexer = Indexer(None)
        indexer.discover_aaai = lambda: [(2025, f"https://x/{n}", f"AAAI-25 Technical Tracks {n}")
                                         for n in range(1, 13) if n != 3]
        _, coverage = indexer.index("AAAI", 2025)
        self.assertEqual(coverage["status"], "failed")
        self.assertIn("Gap", coverage["error"])

    def test_abstract_excludes_reference_sections(self):
        text = "This work evaluates a general optimization method across several mathematical tasks. " * 3
        html = f'<div id="abstract">{text}</div><div id="references">Clinical medical diagnosis cancer</div>'
        self.assertNotIn("Clinical", parse_abstract(html))


class ScreeningAndReports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = Rules(ROOT / "config/medical_topics.json")

    def test_abbreviation_word_boundaries(self):
        result = self.rules.screen(Paper("CVPR", 2025, "Contrastive Learning for Image Retrieval", "url"))
        self.assertEqual(result["decision"], "not_flagged")
        self.assertEqual(self.rules.screen(Paper("ICML", 2025, "EEG Representation Learning", "url"))["decision"], "candidate")

    def test_abstract_only_and_broad_are_not_discarded(self):
        result = self.rules.screen(Paper("ICML", 2025, "A Generic Method", "url", abstract="Evaluated on clinical EHR datasets."))
        self.assertEqual(result["decision"], "review")
        self.assertEqual(self.rules.screen(Paper("ICLR", 2025, "Representation Learning for Brain Signals", "url"))["decision"], "candidate")
        self.assertEqual(self.rules.screen(Paper("CVPR", 2025, "Microscopy Representation Learning", "url"))["decision"], "review")

    def test_pure_biology_exclusion_with_clinical_rescue(self):
        self.assertEqual(self.rules.screen(Paper("ICML", 2025, "Protein Design for Drug Discovery", "url"))["decision"], "out_of_scope")
        self.assertEqual(self.rules.screen(Paper("ICML", 2025, "Protein Language Models for Clinical Diagnosis", "url"))["decision"], "candidate")

    def test_shared_catalog_url_never_suppresses_different_papers(self):
        papers = [Paper("KDD", 2025, "Clinical Paper One", "https://kdd.org/list"),
                  Paper("KDD", 2025, "Clinical Paper Two", "https://kdd.org/list")]
        entries = [{"title": "Clinical Paper One", "url": "https://kdd.org/list", "venue": "KDD", "year": 2025, "line": 1}]
        matches, _ = reconcile(papers, entries)
        self.assertEqual(matches[papers[0].identity]["status"], "already_listed")
        self.assertNotEqual(matches[papers[1].identity]["status"], "already_listed")

    def test_fuzzy_matches_retained_and_wrong_year_reported(self):
        p = Paper("ICML", 2025, "Learning Medical Representations with Fine Grained Supervision", "https://example.org/a")
        near = {"title": "Learning Medical Representations with Fine-Grained Supervisions", "url": "https://x/a", "venue": "ICML", "year": 2025, "line": 4}
        matches, unmatched = reconcile([p], [near])
        self.assertEqual(matches[p.identity]["status"], "possible_match")
        self.assertEqual(unmatched, [near])
        exact = {**near, "title": p.title, "year": 2024}
        matches, _ = reconcile([p], [exact])
        self.assertTrue(matches[p.identity]["placement_mismatch"])

    def test_pdf_aliases(self):
        self.assertEqual(canonical_url("https://openaccess.thecvf.com/content/CVPR2025/papers/A_paper.pdf"),
                         canonical_url("https://openaccess.thecvf.com/content/CVPR2025/html/A_paper.html"))
        self.assertEqual(canonical_url("https://arxiv.org/pdf/2501.01234v2.pdf"), "arxiv:2501.01234")

    def test_wrong_readme_url_does_not_hide_a_paper(self):
        paper = Paper("AAAI", 2025, "Clinical Prediction", "https://ojs.aaai.org/index.php/AAAI/article/view/123")
        entry = {"title": "Entirely Different Paper", "url": paper.url, "venue": "AAAI", "year": 2025, "line": 9}
        matches, unmatched = reconcile([paper], [entry])
        self.assertEqual(matches[paper.identity]["status"], "possible_match")
        self.assertEqual(matches[paper.identity]["url_title_conflicts"][0]["line"], 9)
        self.assertEqual(unmatched, [entry])

    def test_offline_cache_miss_and_failure_visibility(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            client = Client(root / "cache", offline=True)
            papers, status = Indexer(client).index("CVPR", 2025)
            self.assertEqual(status["status"], "failed")
            self.assertIn("Not cached", status["error"])
            readme = root / "README.md"
            readme.write_text("### CVPR 2025\n\n- **[Medical Paper](https://x/paper)** — Summary.\n")
            report = write_reports(papers, [status], self.rules, readme, root / "data", root / "reports", client, [], {})
            self.assertEqual(report["failed_editions"], 1)
            self.assertEqual(len(report["unmatched_readme"]), 1)
            self.assertTrue((root / "reports/coverage.json").exists())

    def test_corrupt_cache_is_not_accepted_offline(self):
        with tempfile.TemporaryDirectory() as directory:
            client = Client(Path(directory), offline=True)
            body, meta = client.paths("https://example.org/catalog")
            body.write_text("truncated catalog")
            meta.write_text(json.dumps({"sha256": "wrong"}))
            with self.assertRaisesRegex(FetchError, "checksum mismatch"):
                client.get("https://example.org/catalog")

    def test_valid_crlf_cache_keeps_original_checksum(self):
        with tempfile.TemporaryDirectory() as directory:
            client = Client(Path(directory), offline=True)
            body, meta = client.paths("https://example.org/catalog")
            content = b"<html>\r\n<p>Paper</p>\r\n</html>"
            body.write_bytes(content)
            meta.write_text(json.dumps({"sha256": hashlib.sha256(content).hexdigest()}))
            self.assertEqual(client.get("https://example.org/catalog").encode(), content)


if __name__ == "__main__":
    unittest.main()
