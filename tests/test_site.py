"""Check published crawl paths, structured data, and project-subpath URLs."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from build_site import Site


class CatalogSite(unittest.TestCase):
    def test_all_internal_paths_resolve_and_titles_are_unique(self):
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)
            site=Site(output=out)
            site.build()
            titles=[]
            for page in out.rglob("*.html"):
                doc=BeautifulSoup(page.read_text(),"html.parser")
                titles.append(doc.title.string)
                self.assertTrue(doc.find("h1"))
                self.assertEqual(len(doc.select('link[rel="canonical"]')),1)
                self.assertTrue(doc.select_one('meta[name="description"]')["content"])
                for node in doc.select("[href], [src]"):
                    url=node.get("href",node.get("src",""))
                    if url.startswith(site.base):
                        relative=unquote(url[len(site.base):].split("#")[0].split("?")[0])
                        target=out/relative
                        if target.is_dir():target=target/"index.html"
                        self.assertTrue(target.exists(),f"{page.name}: {url}")
                for schema in doc.select('script[type="application/ld+json"]'):
                    self.assertEqual(json.loads(schema.string)["@context"],"https://schema.org")
            self.assertEqual(len(titles),len(set(titles)))
            sitemap=ET.parse(out/"sitemap.xml")
            self.assertTrue(all(n.text.startswith(site.base) for n in sitemap.findall(".//{*}loc")))
            conference=BeautifulSoup((out/"conferences/cvpr/index.html").read_text(),"html.parser")
            self.assertEqual(len(conference.select("article.paper")),sum(r["venue"]=="CVPR" for r in site.rows))
            self.assertEqual(len(json.loads((out/"data/papers.json").read_text())),len(site.rows))


if __name__=="__main__":
    unittest.main()
