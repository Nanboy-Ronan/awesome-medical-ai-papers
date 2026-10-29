"""Source-specific parsers. Membership comes from complete official catalogs.

Virtual conference exports supplement abstracts, but do not silently add papers
absent from proceedings. ICLR 2023 has no proceedings.iclr.cc catalog; its
official accepted-presentation export is the explicitly reported fallback.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import threading
import time
import unicodedata
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import requests


VENUES = ("CVPR", "NeurIPS", "ICML", "ICLR", "ICCV", "ECCV", "ACL", "EMNLP", "NAACL", "AAAI", "KDD")
YEARS = (2023, 2024, 2025)


def clean(value: str) -> str:
    return " ".join(html.unescape(value or "").split())


def key(title: str) -> str:
    title = unicodedata.normalize("NFKD", clean(title)).casefold()
    # Preserve word content while ignoring punctuation, accents, and LaTeX markup.
    title = re.sub(r"\\(?:texttt|textbf|mathrm|mathcal|textrm|text|emph)\b", "", title)
    return "".join(c for c in title if c.isalnum())


def soup(document: str) -> BeautifulSoup:
    return BeautifulSoup(document, "html.parser")


@dataclass
class Paper:
    venue: str
    year: int
    title: str
    url: str
    track: str = "main"
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    abstract_source: str = ""
    sources: list[str] = field(default_factory=list)
    alternate_urls: list[str] = field(default_factory=list)

    @property
    def identity(self) -> str:
        return f"{self.venue}:{self.year}:{key(self.title)}"

    def to_dict(self) -> dict:
        return {"id": self.identity, **asdict(self)}


def deduplicate(papers: list[Paper]) -> list[Paper]:
    result: dict[str, Paper] = {}
    for paper in papers:
        existing = result.get(paper.identity)
        if existing is None:
            result[paper.identity] = paper
            continue
        if not existing.abstract and paper.abstract:
            existing.abstract = paper.abstract
            existing.abstract_source = paper.abstract_source
        if not existing.authors:
            existing.authors = paper.authors
        existing.sources = sorted(set(existing.sources + paper.sources))
        existing.alternate_urls = sorted(set(existing.alternate_urls + paper.alternate_urls + [paper.url]) - {existing.url})
    return list(result.values())


class FetchError(RuntimeError):
    pass


class Client:
    """Cached, bounded, polite HTTP; blocked/empty pages never count as success."""

    def __init__(self, cache: Path, *, offline=False, refresh=False, delay=0.5, timeout=60):
        self.cache = cache
        self.offline = offline
        self.refresh = refresh
        self.delay = delay
        self.timeout = timeout
        self.lock = threading.Lock()
        self.next_request: dict[str, float] = defaultdict(float)
        self.used: dict[str, dict] = {}
        cache.mkdir(parents=True, exist_ok=True)

    def paths(self, url: str) -> tuple[Path, Path]:
        stem = hashlib.sha256(url.encode()).hexdigest()
        return self.cache / f"{stem}.body", self.cache / f"{stem}.json"

    def get(self, url: str) -> str:
        body, meta = self.paths(url)
        if body.exists() and meta.exists() and (self.offline or not self.refresh):
            # Keep exact line endings: universal-newline text reads would make
            # a valid CRLF response disagree with its recorded checksum.
            document = body.read_bytes().decode("utf-8")
            metadata = json.loads(meta.read_text(encoding="utf-8"))
            if hashlib.sha256(document.encode()).hexdigest() == metadata.get("sha256"):
                with self.lock:
                    self.used[url] = {**metadata, "cached": True}
                return document
            if self.offline:
                raise FetchError(f"Cache checksum mismatch: {url}")
        if self.offline:
            raise FetchError(f"Not cached in offline mode: {url}")
        host = urlparse(url).netloc
        error: Exception | None = None
        for attempt in range(3):
            with self.lock:
                wait = max(0.0, self.next_request[host] - time.monotonic())
                self.next_request[host] = time.monotonic() + wait + self.delay
            time.sleep(wait)
            try:
                response = requests.get(url, timeout=self.timeout, headers={
                    "User-Agent": "awesome-medical-ai-papers-indexer/1.0 (public research metadata)",
                    "Accept": "application/json, application/xml, text/html;q=0.9, */*;q=0.8",
                })
                if response.status_code != 200:
                    raise FetchError(f"HTTP {response.status_code}: {url}")
                document = response.content.decode("utf-8-sig", errors="replace")
                if not document.strip() or any(t in document[:8000].lower() for t in (
                    "making sure you&#39;re not a bot", "just a moment...", "cf-chl-", "access denied")):
                    raise FetchError(f"Empty or access-challenge response: {url}")
                metadata = {"url": url, "resolved_url": response.url,
                            "fetched_at": datetime.now(timezone.utc).isoformat(),
                            "sha256": hashlib.sha256(document.encode()).hexdigest(), "bytes": len(response.content)}
                # Per-URL writes are serialized; readers never see a partial cache pair.
                with self.lock:
                    body.write_bytes(document.encode("utf-8"))
                    meta.write_text(json.dumps(metadata, indent=2) + "\n")
                    self.used[url] = {**metadata, "cached": False}
                return document
            except (requests.RequestException, FetchError) as exc:
                error = exc
                if attempt < 2:
                    time.sleep(2 ** attempt)
        raise FetchError(f"{url}: {error}")


def parse_cvf(document: str, url: str, venue: str, year: int) -> list[Paper]:
    result = []
    for node in soup(document).select("dt.ptitle"):
        anchor = node.find("a", href=True)
        if not anchor:
            raise FetchError(f"Paper title without a link in {url}")
        target = urljoin(url, anchor["href"])
        # Exclude workshops even if linked from the main catalog.
        if venue != "ECCV" and f"/content/{venue}{year}/html/" not in target:
            continue
        if venue == "ECCV" and f"eccv_{year}/" not in target:
            continue
        author_node = node.find_next_sibling("dd")
        inputs = author_node.select('input[name="query_author"]') if author_node else []
        authors = [clean(n.get("value", "")) for n in inputs]
        if not authors and venue == "ECCV" and author_node:
            authors = clean(author_node.get_text(" ")).split(", ")
        result.append(Paper(venue, year, clean(anchor.get_text(" ")), target, authors=authors, sources=[url]))
    return deduplicate(result)


def parse_neural(document: str, url: str, venue: str, year: int) -> tuple[list[Paper], int | None]:
    tree = soup(document)
    result = []
    for li in tree.select(".paper-list li"):
        anchor = li.select_one('a[href*="/hash/"]')
        if anchor is None:
            raise FetchError(f"Unparsed proceedings list item in {url}")
        target = urljoin(url, anchor["href"])
        if "Creative_AI" in target:
            continue
        track = "datasets-and-benchmarks" if "Datasets_and_Benchmarks" in target else "main"
        authors = li.select_one(".paper-authors") or li.find("span")
        result.append(Paper(venue, year, clean(anchor.get_text(" ")), target, track,
                            clean(authors.get_text(" ")).split(", ") if authors else [], sources=[url]))
    declared = re.search(r"\b([\d,]+) papers\b", tree.get_text(" ", strip=True))
    return deduplicate(result), int(declared[1].replace(",", "")) if declared else None


def parse_pmlr(document: str, url: str, year: int) -> list[Paper]:
    result = []
    for node in soup(document).select("div.paper"):
        title = node.select_one(".title")
        anchor = next((a for a in node.select("a[href]") if a.get_text(strip=True) == "abs"), None)
        if title is None or anchor is None:
            raise FetchError(f"Unparsed PMLR paper block in {url}")
        authors = node.select_one(".authors")
        result.append(Paper("ICML", year, clean(title.get_text(" ")), urljoin(url, anchor["href"]),
                            authors=clean(authors.get_text(" ")).split(", ") if authors else [], sources=[url]))
    return deduplicate(result)


def parse_virtual(document: str, url: str, venue: str, year: int) -> tuple[list[Paper], int]:
    obj = json.loads(document)
    records = obj["results"] if isinstance(obj, dict) else obj
    if isinstance(obj, dict) and (obj.get("next") or obj.get("count", len(records)) != len(records)):
        raise FetchError(f"Incomplete/paginated virtual export: {url}")
    result = []
    for row in records:
        if row.get("eventtype", "").lower() not in ("poster", "oral", "spotlight"):
            continue
        title = clean(row.get("name") or row.get("title", ""))
        if not title:
            raise FetchError(f"Missing title in virtual export: {url}")
        target = row.get("paper_url") or urljoin(url, row.get("virtualsite_url", ""))
        abstract = clean(row.get("abstract", ""))
        result.append(Paper(venue, year, title, target,
                            authors=[clean(a.get("fullname", "")) for a in row.get("authors", [])],
                            abstract=abstract, abstract_source=url if abstract else "", sources=[url]))
    return deduplicate(result), len(records)


def parse_acl(document: str, url: str, venue: str, year: int, include_findings=False) -> list[Paper]:
    root = ET.fromstring(document)
    if root.attrib.get("id") != f"{year}.{venue.lower()}":
        raise FetchError(f"Unexpected ACL collection at {url}")
    result = []
    allowed = {"long", "short", "main"}
    if include_findings:
        allowed.add("findings")
    for volume in root.findall("volume"):
        volume_id = volume.attrib["id"]
        if volume_id not in allowed:
            continue
        for node in volume.findall("paper"):
            title = clean("".join(node.find("title").itertext()))
            paper_id = f"{year}.{venue.lower()}-{volume_id}.{node.attrib['id']}"
            abstract_node = node.find("abstract")
            abstract = clean("".join(abstract_node.itertext())) if abstract_node is not None else ""
            authors = [clean(" ".join("".join(n.itertext()) for n in author)) for author in node.findall("author")]
            result.append(Paper(venue, year, title, f"https://aclanthology.org/{paper_id}/", volume_id, authors,
                                abstract, url if abstract else "", [url]))
    return deduplicate(result)


def parse_aaai_archive(document: str, url: str) -> tuple[list[tuple[int, str, str]], str | None]:
    tree = soup(document)
    issues = []
    for a in tree.select("a.title[href]"):
        label = clean(a.get_text(" "))
        match = re.search(r"AAAI-(\d{2})\b", label)
        if match:
            issues.append((2000 + int(match[1]), urljoin(url, a["href"]), label))
    next_page = tree.select_one("a.next[href]")
    return issues, urljoin(url, next_page["href"]) if next_page else None


def parse_aaai_issue(document: str, url: str, year: int) -> list[Paper]:
    tree = soup(document)
    result = []
    for node in tree.select(".obj_article_summary"):
        a = node.select_one(".title a[href]")
        if a is None:
            raise FetchError(f"Article without title/link in {url}")
        # Article section is the accurate track, even inside a mixed volume.
        section = node.find_parent("div", class_="section")
        heading = section.find(["h2", "h3"]) if section else None
        track = clean(heading.get_text(" ")) if heading else "technical"
        authors = node.select_one(".authors")
        result.append(Paper("AAAI", year, clean(a.get_text(" ")), urljoin(url, a["href"]), track,
                            clean(authors.get_text(" ")).split(", ") if authors else [], sources=[url]))
    return deduplicate(result)


def parse_kdd(document: str, url: str, year: int, track: str) -> list[Paper]:
    tree = soup(document)
    result = []
    if year == 2023:
        nodes = tree.select(".entry-content h5")
        for node in nodes:
            title = clean(node.get_text(" "))
            if len(title) < 12:
                continue
            author = node.find_next_sibling("p")
            result.append(Paper("KDD", year, title, url, track,
                                [clean(author.get_text(" "))] if author else [], sources=[url]))
    else:
        for cell in tree.select("table td"):
            strong = cell.find("strong")
            if not strong:
                continue
            title = clean(strong.get_text(" "))
            if len(title) < 12:
                continue
            doi = re.search(r"10\.1145/[\d.]+", cell.get_text(" "))
            target = f"https://doi.org/{doi[0].rstrip('.')}" if doi else url
            title_row = cell.find_parent("tr")
            author_row = title_row.find_next_sibling("tr") if title_row else None
            author_text = clean(author_row.get_text(" ")) if author_row else ""
            if author_row and author_row.find("strong"):
                author_text = ""
            result.append(Paper("KDD", year, title, target, track,
                                [clean(a) for a in author_text.split(";")] if author_text else [], sources=[url]))
    return deduplicate(result)


def supplement(papers: list[Paper], abstracts: list[Paper]) -> int:
    by_title = {key(p.title): p for p in abstracts}
    matched = 0
    for paper in papers:
        other = by_title.get(key(paper.title))
        if other is None:
            continue
        matched += 1
        if other.abstract and not paper.abstract:
            paper.abstract = other.abstract
            paper.abstract_source = other.abstract_source
        if not paper.authors:
            paper.authors = other.authors
        paper.sources = sorted(set(paper.sources + other.sources))
        if other.url != paper.url:
            paper.alternate_urls = sorted(set(paper.alternate_urls + [other.url]))
    return matched


def bulk_url(venue: str, year: int) -> str:
    domains = {"CVPR": "cvpr.thecvf.com", "ICCV": "iccv.thecvf.com", "ECCV": "eccv.ecva.net",
               "NeurIPS": "neurips.cc", "ICLR": "iclr.cc", "ICML": "icml.cc"}
    return f"https://{domains[venue]}/static/virtual/data/{venue.lower()}-{year}-orals-posters.json"


def edition_exists(venue: str, year: int) -> bool:
    return not ((venue == "ICCV" and year % 2 == 0) or (venue == "ECCV" and year % 2 == 1)
                or (venue == "NAACL" and year == 2023))


class Indexer:
    def __init__(self, client: Client, *, include_findings=False):
        self.client = client
        self.include_findings = include_findings
        self.aaai_lock = threading.Lock()
        self.aaai_issues: list[tuple[int, str, str]] | None = None
        self.aaai_archives: list[str] = []

    def discover_aaai(self, oldest: int = 2023) -> list[tuple[int, str, str]]:
        with self.aaai_lock:
            if self.aaai_issues is not None:
                return self.aaai_issues
            issues = []
            page = "https://ojs.aaai.org/index.php/AAAI/issue/archive"
            visited = set()
            while page:
                if page in visited or len(visited) >= 40:
                    raise FetchError("AAAI archive pagination loop/limit")
                visited.add(page)
                self.aaai_archives.append(page)
                found, next_page = parse_aaai_archive(self.client.get(page), page)
                issues.extend(found)
                # Archive is newest first; stop only once a strictly older year appears.
                if found and min(y for y, _, _ in found) < oldest:
                    break
                page = next_page
            self.aaai_issues = list(dict.fromkeys(issues))
            return self.aaai_issues

    def index(self, venue: str, year: int) -> tuple[list[Paper], dict]:
        coverage = {"venue": venue, "year": year, "status": "not_held" if not edition_exists(venue, year) else "failed",
                    "sources": [], "notes": [], "expected_count": None, "catalog_kind": "official_proceedings"}
        if not edition_exists(venue, year):
            return [], coverage
        papers: list[Paper] = []
        try:
            if venue in ("CVPR", "ICCV"):
                url = f"https://openaccess.thecvf.com/{venue}{year}?day=all"
                coverage["sources"].append(url)
                papers = parse_cvf(self.client.get(url), url, venue, year)
            elif venue == "ECCV":
                url = "https://www.ecva.net/papers.php"
                coverage["sources"].append(url)
                papers = parse_cvf(self.client.get(url), url, venue, year)
            elif venue in ("NeurIPS", "ICLR") and not (venue == "ICLR" and year == 2023):
                domain = "proceedings.neurips.cc" if venue == "NeurIPS" else "proceedings.iclr.cc"
                url = f"https://{domain}/paper_files/paper/{year}"
                # In 2025 the bare NeurIPS year route points to Creative AI.
                if venue == "NeurIPS" and year == 2025:
                    url += "/vol38-main-conference"
                coverage["sources"].append(url)
                papers, declared = parse_neural(self.client.get(url), url, venue, year)
                coverage["expected_count"] = declared
                if declared is not None and declared != len(papers):
                    raise FetchError(f"Catalog says {declared} papers but parsed {len(papers)}")
            elif venue == "ICLR":
                url = bulk_url(venue, year)
                coverage["sources"].append(url)
                papers, raw_count = parse_virtual(self.client.get(url), url, venue, year)
                coverage["catalog_kind"] = "official_accepted_presentations"
                coverage["notes"].append("ICLR 2023 has no proceedings.iclr.cc year catalog; uses official accepted presentations, deduplicating oral/poster entries.")
                coverage["raw_presentation_count"] = raw_count
            elif venue == "ICML":
                volume = {2023: 202, 2024: 235, 2025: 267}[year]
                url = f"https://proceedings.mlr.press/v{volume}/"
                coverage["sources"].append(url)
                papers = parse_pmlr(self.client.get(url), url, year)
            elif venue in ("ACL", "EMNLP", "NAACL"):
                url = f"https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{year}.{venue.lower()}.xml"
                coverage["sources"].append(url)
                papers = parse_acl(self.client.get(url), url, venue, year)
                if self.include_findings:
                    findings = f"https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{year}.findings-{venue.lower()}.xml"
                    coverage["sources"].append(findings)
                    papers += self.index_findings(findings, venue, year)
            elif venue == "AAAI":
                issues = self.discover_aaai()
                selected = [(u, label) for y, u, label in issues if y == year]
                # Mixed special-track volumes are retained, with section-level labels.
                # Co-located IAAI/EAAI and student-only volumes are explicitly excluded.
                selected = [(u, label) for u, label in selected if re.match(r"AAAI-\d+ (?:Technical|Special)", label)]
                if len(selected) < 10:
                    raise FetchError(f"Only {len(selected)} AAAI issues discovered; archive may be incomplete")
                numbers = {int(m[1]) for _, label in selected
                           if (m := re.search(r"Technical Tracks? (\d+)\b", label))}
                if not numbers or numbers != set(range(1, max(numbers) + 1)):
                    raise FetchError(f"Gap in AAAI technical volume numbering: {sorted(numbers)}")
                coverage["archive_pages"] = self.aaai_archives.copy()
                coverage["notes"].append("Includes technical and special-track volumes, retaining section labels; excludes co-located IAAI/EAAI and student-only volumes.")
                for url, _ in selected:
                    coverage["sources"].append(url)
                    part = parse_aaai_issue(self.client.get(url), url, year)
                    if not part:
                        raise FetchError(f"No articles in AAAI issue: {url}")
                    papers.extend(part)
                coverage["issue_count"] = len(selected)
            elif venue == "KDD":
                coverage["catalog_kind"] = "official_accepted_paper_lists"
                tracks = [("research", "research-track-papers"), ("applied-data-science", "ads-track-papers" if year == 2023 else "applied-data-science-track-papers")]
                if year == 2025:
                    tracks = [("research", "research-track-papers-2"), ("applied-data-science", "applied-data-science-ads-track-papers-2"), ("datasets-and-benchmarks", "datasets-and-benchmarks-track-papers-2")]
                for track, slug in tracks:
                    url = f"https://{'www.' if year == 2025 else ''}kdd.org/kdd{year}/{slug}/" + ("index.html" if year == 2023 else "")
                    coverage["sources"].append(url)
                    part = parse_kdd(self.client.get(url), url, year, track)
                    if len(part) < 10:
                        raise FetchError(f"Too few KDD {track} papers: {len(part)} at {url}")
                    papers.extend(part)
                coverage["notes"].append("Official Research/ADS lists, plus Datasets & Benchmarks in 2025; papers without a supplied DOI link to the catalog and need paper-specific link verification.")
            papers = deduplicate(papers)
            if len(papers) < 100:
                raise FetchError(f"Suspiciously small catalog ({len(papers)} papers)")
            coverage["status"] = "indexed"
            if venue in ("CVPR", "ICCV", "ECCV", "NeurIPS", "ICML", "ICLR") and not (venue == "ICLR" and year == 2023):
                url = bulk_url(venue, year)
                coverage["supplement_url"] = url
                try:
                    supplemental, raw_count = parse_virtual(self.client.get(url), url, venue, year)
                    matched = supplement(papers, supplemental)
                    coverage["supplement_unique_count"] = len(supplemental)
                    coverage["supplement_raw_count"] = raw_count
                    coverage["supplement_matched_count"] = matched
                    if matched < len(papers):
                        coverage["notes"].append(f"Bulk abstracts matched {matched}/{len(papers)} proceedings titles; unmatched titles remain indexed.")
                except (FetchError, ValueError, KeyError) as exc:
                    coverage["notes"].append(f"Abstract supplement unavailable: {exc}")
        except (FetchError, ValueError, KeyError, ET.ParseError) as exc:
            coverage["status"] = "failed"
            coverage["error"] = str(exc)
        coverage["paper_count"] = len(papers)
        coverage["abstract_count"] = sum(bool(p.abstract) for p in papers)
        coverage["count_check"] = ("matches_declared_total" if coverage["status"] == "indexed" and coverage["expected_count"] is not None
                                   else "no_independent_total" if coverage["status"] == "indexed" else "not_verified")
        return papers, coverage

    def index_findings(self, url: str, venue: str, year: int) -> list[Paper]:
        root = ET.fromstring(self.client.get(url))
        expected = f"{year}.findings-{venue.lower()}"
        if root.attrib.get("id") != expected:
            raise FetchError(f"Unexpected Findings collection: {url}")
        result = []
        for volume in root.findall("volume"):
            for node in volume.findall("paper"):
                title = clean("".join(node.find("title").itertext()))
                a = node.find("abstract")
                abstract = clean("".join(a.itertext())) if a is not None else ""
                result.append(Paper(venue, year, title, f"https://aclanthology.org/{expected}.{node.attrib['id']}/",
                                    "findings", abstract=abstract, abstract_source=url if abstract else "", sources=[url]))
        return result
