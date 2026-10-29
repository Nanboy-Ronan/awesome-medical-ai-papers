#!/usr/bin/env python3
"""Build a crawlable GitHub Pages catalog from README and committed research outputs."""

from collections import Counter, defaultdict
import csv
from html import escape as h
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

from paper_index.pipeline import read_readme
from paper_index.sources import key

ROOT = Path(__file__).resolve().parents[1]


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def load_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def embedded_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")


class Site:
    def __init__(self, root=ROOT, output=None):
        self.root = root
        self.output = output or root / "_site"
        self.config = json.loads((root / "config/site.json").read_text())
        self.base = self.config["base_url"]
        self.repo = self.config["repository"]
        self.report = root / "reports/analysis"
        self.summary = json.loads((self.report / "summary.json").read_text())
        self.rows = load_csv(self.report / "medical_papers.csv")
        readme = read_readme(root / "README.md")
        if {(r['venue'],int(r['year']),key(r['title'])) for r in self.rows} != {(r['venue'],r['year'],key(r['title'])) for r in readme}:
            raise ValueError("Analysis corpus is stale relative to README; rerun analyze_research.py")
        descriptions = {}
        for line in (root / "README.md").read_text().splitlines():
            match = re.match(r"- \*\*\[(.+?)\]\(https?://[^\s)]+\)\*\*.*? — (.+)", line)
            if match:
                descriptions[key(match[1])] = re.sub(r"\s*\*\[[^\]]+\]\*\s*$", "", match[2]).strip()
        for row in self.rows:
            row["year"] = int(row["year"])
            row["summary"] = descriptions.get(key(row["title"]), "")
            row["domains"] = row["domains"].split("; ") if row["domains"] else []
            row["methods"] = row["methods"].split("; ") if row["methods"] else []
        self.rows.sort(key=lambda r: (-r["year"], r["venue"], key(r["title"])))
        self.urls = []

    def url(self, path=""):
        return urljoin(self.base, path)

    def layout(self, path, title, description, body, schema=None, script=False):
        canonical = self.url(path)
        dataset = {"@context": "https://schema.org", "@type": "CollectionPage", "name": title,
                   "description": description, "url": canonical, "isPartOf": {"@type": "WebSite", "name": self.config["name"], "url": self.base}}
        document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h(title)} | Awesome Medical AI Papers</title><meta name="description" content="{h(description, quote=True)}">
<link rel="canonical" href="{h(canonical)}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:title" content="{h(title,quote=True)}">
<meta property="og:description" content="{h(description,quote=True)}"><meta property="og:url" content="{h(canonical)}">
<meta property="og:image" content="{self.url('assets/social-card.png')}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{h(title,quote=True)}">
<meta name="twitter:description" content="{h(description,quote=True)}"><meta name="twitter:image" content="{self.url('assets/social-card.png')}">
<meta name="theme-color" content="#0f172a"><link rel="icon" href="{self.url('assets/favicon.svg')}" type="image/svg+xml">
<link rel="stylesheet" href="{self.url('assets/styles.css')}">
<script type="application/ld+json">{embedded_json(schema or dataset)}</script>
</head><body><a class="skip" href="#main">Skip to content</a>
<header><a class="brand" href="{self.base}"><span class="brand-mark">m+</span> Medical AI Papers</a>
<nav aria-label="Main navigation"><a href="{self.url('research/')}">Research</a><a href="{self.url('about/')}">Methodology</a><a class="star" href="{self.repo}">☆ Star on GitHub</a></nav></header>
<main id="main">{body}</main><footer><p>An open research resource. Papers and original research belong to their authors.</p>
<p><a href="{self.repo}">GitHub</a> · <a href="{self.repo}/blob/main/CITATION.cff">Cite this resource</a> · <a href="{self.url('data/medical_papers.csv')}">Download CSV</a> · <a href="{self.url('llms.txt')}">Source guide</a> · <a href="{self.url('sitemap.xml')}">Sitemap</a></p>
<p>Maintained by the Awesome Medical AI Papers contributors. No claim of exhaustive coverage or guaranteed clinical effectiveness.</p></footer>
{f'<script src="{self.url("assets/app.js")}" defer data-catalog="{self.url("data/papers.json")}"></script>' if script else ''}
</body></html>'''
        target = self.output / (path + "index.html" if path.endswith("/") or not path else path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(document, encoding="utf-8")
        self.urls.append(canonical)

    def cards(self, rows):
        cards = []
        for row in rows:
            tags = f'<a href="{self.url("conferences/"+slug(row["venue"])+"/")}">{h(row["venue"])}</a><a href="{self.url("years/"+str(row["year"])+"/")}">{row["year"]}</a>'
            methods = "".join(f'<span>{h(m)}</span>' for m in row["methods"][:3])
            summary = h(row["summary"]).replace("**", "").replace("*", "")
            cards.append(f'<article class="paper"><div class="paper-meta">{tags}</div><h3><a href="{h(row["url"],quote=True)}">{h(row["title"])}</a></h3><p>{summary}</p><div class="tags">{methods}</div></article>')
        return "\n".join(cards)

    def listing(self, path, title, rows, intro):
        counts = Counter(row["year"] for row in rows)
        years = " · ".join(f'{y}: {counts[y]}' for y in sorted(counts))
        self.layout(path, title, f"Browse {len(rows)} curated {title.lower()} with official paper links, publication years, summaries, and research topics.",
                    f'<section class="page-heading"><p class="eyebrow">The research catalog</p><h1>{h(title)}</h1><p>{h(intro)}</p><p class="muted">{len(rows):,} papers · {years}</p></section><section class="papers" aria-label="Papers">{self.cards(rows)}</section>')

    def data_table(self, headers, rows):
        return '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{h(str(v))}</th>' for v in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{h(str(v))}</td>' for v in row) + '</tr>' for row in rows) + '</tbody></table></div>'

    def homepage(self):
        by_venue = Counter(row["venue"] for row in self.rows)
        by_domain = Counter(d for row in self.rows for d in row["domains"])
        venue_links = ''.join(f'<a class="browse-link" href="{self.url("conferences/"+slug(v)+"/")}"><strong>{v}</strong><span>{n} papers ↗</span></a>' for v,n in sorted(by_venue.items()))
        topic_links = ''.join(f'<a class="browse-link" href="{self.url("topics/"+slug(t)+"/")}"><strong>{h(t)}</strong><span>{n} title matches ↗</span></a>' for t,n in by_domain.most_common())
        year_links = ''.join(f'<a class="year-link" href="{self.url("years/"+str(y)+"/")}">{y} <span>{sum(r["year"]==y for r in self.rows)} papers</span> ↗</a>' for y in (2025,2024,2023))
        options = ''.join(f'<option>{v}</option>' for v in sorted(by_venue))
        body = f'''<section class="hero"><p class="eyebrow">Evidence before hype · 2023–2025</p><h1>The medical AI<br>research landscape.</h1>
<p class="lead">A curated guide to medical imaging, clinical language models, pathology, brain AI, and healthcare research at major CS/AI conferences.</p>
<div class="hero-actions"><a class="button" href="#catalog">Find a paper ↓</a><a class="button secondary" href="{self.url('research/')}">Explore the research ↗</a></div>
<div class="stat-strip"><div><strong>{len(self.rows):,}</strong><span>curated papers</span></div><div><strong>{len(by_venue)}</strong><span>conference families</span></div><div><strong>3</strong><span>publication years</span></div></div></section>
<section class="section"><div class="section-title"><h2>Browse by conference</h2><p>Official titles. Publication years. Paper-specific sources.</p></div><div class="browse-grid">{venue_links}</div><div class="year-grid">{year_links}</div></section>
<section class="research-band"><p class="eyebrow">The data behind the list</p><h2>How much medical AI gets published?<br>What changed over three years?</h2>
<p>Reproducible studies of proceedings shares, ICLR submission decisions, and topic trends. Every chart comes with counts, code, and explicit denominators.</p>
<div class="research-grid"><a href="{self.url('research/medical-share/')}"><strong>01 / Publication share</strong><span>Conference-by-year counts and coverage limits ↗</span></a><a href="{self.url('research/acceptance-rates/')}"><strong>02 / ICLR decision rates</strong><span>Medical-keyword versus other-title comparisons ↗</span></a><a href="{self.url('research/topics/')}"><strong>03 / Topics & methods</strong><span>Yearly domains, approaches, and keywords ↗</span></a></div></section>
<section class="section" id="catalog"><div class="section-title"><h2>Find your next paper</h2><p>Search titles, summaries, and research labels. Results link to original papers.</p></div>
<form class="search-controls" role="search" id="paper-search"><label>Search<input type="search" id="query" placeholder="e.g. radiology, diffusion, medical LLM" autocomplete="off"></label><label>Conference<select id="venue"><option value="">All conferences</option>{options}</select></label><label>Year<select id="year"><option value="">All years</option><option>2025</option><option>2024</option><option>2023</option></select></label></form>
<p class="muted" id="result-count" role="status">A selection of recent papers. Enable JavaScript to search the complete catalog.</p><div id="search-results" class="papers">{self.cards(self.rows[:12])}</div><button class="button secondary" id="show-more" hidden>Show more papers</button>
<noscript><p>All papers remain available without JavaScript through the conference, year, and topic pages.</p></noscript></section>
<section class="section"><div class="section-title"><h2>Browse research domains</h2><p>Multi-label title rules; a paper may belong to more than one domain.</p></div><div class="browse-grid topics">{topic_links}</div></section>
<section class="faq"><h2>Questions about the collection</h2><details><summary>What is included?</summary><p>Medical AI and healthcare papers from CVPR, NeurIPS, ICML, ICLR, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, and KDD in 2023–2025. Research datasets, benchmarks, and named special tracks are labeled. Specialist medical conferences, workshops, doctoral abstracts, and pure molecular discovery are outside this snapshot.</p></details>
<details><summary>Is the list exhaustive?</summary><p>No. We index full conference catalogs before screening, then curate relevant papers. Broader candidates remain in a public review queue. The observed medical shares are lower bounds within the indexed corpus.</p></details>
<details><summary>Are publication shares acceptance rates?</summary><p>No. A publication share divides medical accepted papers by all accepted papers. A submission acceptance rate requires accepted and rejected submissions. Our decision-rate study is limited to ICLR public snapshots.</p></details>
<details><summary>How can I contribute or cite this?</summary><p>Submit a paper with its official title, conference year, paper-specific source, and a short summary through <a href="{self.repo}/issues/new/choose">GitHub</a>. Use <a href="{self.repo}/blob/main/CITATION.cff">CITATION.cff</a> for attribution. If the resource helps your work, a GitHub star makes it easy to bookmark and discover.</p></details></section>'''
        schema = {"@context":"https://schema.org", "@type":"Dataset", "name":self.config["name"],
                  "description":self.config["description"], "url":self.base, "sameAs":self.repo,
                  "license":"https://creativecommons.org/publicdomain/zero/1.0/", "temporalCoverage":"2023/2025",
                  "keywords":["medical AI","healthcare AI","conference papers","medical imaging","clinical NLP"],
                  "creator":{"@type":"Organization","name":"Awesome Medical AI Papers contributors","url":self.repo},
                  "measurementTechnique":"Proceedings metadata indexing, recorded curation decisions, and deterministic title-based annotation",
                  "distribution":[{"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":self.url("data/medical_papers.csv")}],
                  "isBasedOn":self.url("about/")}
        self.layout("", "Medical AI & Healthcare AI Conference Papers, 2023–2025", self.config["description"], body, schema, script=True)

    def research_pages(self):
        links = ''.join(f'<a class="browse-link" href="{self.url("research/"+path+"/")}"><strong>{title}</strong><span>{desc} ↗</span></a>' for path,title,desc in (
            ("medical-share","Medical share of proceedings","By conference, track, and year"),
            ("acceptance-rates","ICLR medical versus other-title decision rates","Explicit status and denominator definitions"),
            ("topics","Topics, methods, and keywords","Title-based domain and method prevalence")))
        self.layout("research/", "Medical AI Research Trends & Conference Statistics", "Reproducible 2023–2025 medical AI conference statistics, ICLR decision-rate comparisons, and topic analysis with CSV data and methodology.",
                    f'<section class="page-heading"><p class="eyebrow">Three studies · open data · reproducible code</p><h1>Research on the research.</h1><p>Understand this collection through publication counts, submission decisions, and title-based research trends. Each study makes its scope and limitations explicit.</p></section><div class="browse-grid topics">{links}</div>')
        shares = self.summary["yearly"]
        share_table = self.data_table(["Year","Curated medical","Eligible indexed papers","Observed medical share"], [(r["year"],r["curated_medical_records"],r["eligible_research_records"],f'{r["curated_share_pct"]:.2f}%') for r in shares])
        details = load_csv(self.report / "conference_year_shares.csv")
        details_table = self.data_table(["Conference","Year","Curated medical","Eligible research","Share"], [(r["venue"],r["year"],r["curated_eligible_medical"],r["eligible_research_records"],f'{float(r["curated_share_of_eligible_pct"]):.2f}%') for r in details])
        self.layout("research/medical-share/", "Medical AI Share of Conference Papers by Year, 2023–2025", "Observed curated medical AI shares by conference and publication year, with research-only denominators, track breakdowns, and coverage limitations.",
                    f'<section class="page-heading"><p class="eyebrow">Study 01 · Descriptive corpus analysis</p><h1>Medical AI as a share of conference papers.</h1><p class="notice">These are lower-bound shares of the indexed corpus, not submission acceptance rates. Coverage and venue mix can change the result.</p></section>{share_table}<figure><img src="{self.url("figures/medical-share.svg")}" alt="Observed curated medical shares of indexed eligible research papers in 2023, 2024, and 2025; these are not submission acceptance rates."></figure><h2>Conference and year breakdown</h2>{details_table}<figure><img loading="lazy" src="{self.url("figures/conference-shares.svg")}" alt="Heatmap of curated medical shares by conference and year; editions not held are marked separately."></figure><p>Research-only counts exclude nonresearch formats in mixed AAAI volumes. NeurIPS and KDD research/benchmark tracks remain included, with separate track counts. Alternating editions and incomplete curation limit longitudinal interpretation.</p><p><a href="{self.repo}/blob/main/reports/analysis/medical-share.md">Full study and venue-mix sensitivity ↗</a> · <a href="{self.url("data/conference_year_shares.csv")}">Download counts</a></p>')
        rates = [r for r in self.summary["acceptance_rates"] if r["definition"]=="specific_title_proxy"]
        rate_table = self.data_table(["Year","Title group","Accept","Reject","Conditional decision rate","95% Wilson interval"], [(r["year"],r["group"],r["accepted"],r["rejected"],f'{r["decision_rate_pct"]:.2f}%',f'{r["wilson95_low_pct"]:.1f}–{r["wilson95_high_pct"]:.1f}%') for r in rates])
        self.layout("research/acceptance-rates/", "Medical AI Acceptance Rates vs Other Titles: ICLR 2023–2025", "ICLR public-snapshot comparison of medical-keyword and other-title accepted/rejected decisions, with classifier sensitivity and explicit source limits.",
                    f'<section class="page-heading"><p class="eyebrow">Study 02 · ICLR snapshot comparison</p><h1>Medical-keyword titles and ICLR decisions.</h1><p class="notice">Accepted / (accepted + rejected) final decisions. Withdrawn and desk-rejected submissions are excluded from this denominator. This is not the official conference acceptance rate.</p></section><p>Apply the same specific medical title rule to both accepted and rejected submissions. Other titles may include missed medical research. Source: <a href="https://github.com/papercopilot/paperlists/tree/9fcfd1234879a8e5630b5116dde411ec143dd763">Paper Copilot’s pinned historical OpenReview snapshots</a>, not a live official census.</p>{rate_table}<figure><img src="{self.url("figures/iclr-decision-rates.svg")}" alt="Conditional ICLR decision rates for medical-keyword and other-title groups, 2023 to 2025, with Wilson intervals."></figure><p>The groups differ in title wording and can differ in many unmeasured ways. These observational results do not establish reviewer preference or a causal disadvantage for medical research. Small medical-title groups have substantial uncertainty.</p><p><a href="{self.repo}/blob/main/reports/analysis/acceptance-rates.md">Full study, official baselines, and limitations ↗</a> · <a href="{self.url("data/acceptance_rates.csv")}">Download all rate definitions</a> · <a href="{self.url("data/acceptance_by_area.csv")}">Other research areas</a></p>')
        topics = load_csv(self.report / "topic_trends.csv")
        topic_tables = []
        for family in ("domain","method"):
            names = sorted({r["topic"] for r in topics if r["family"]==family})
            lookup = {(r["topic"],int(r["year"])):r for r in topics if r["family"]==family}
            topic_tables.append(f'<h2>{"Research domains" if family=="domain" else "Research methods"}</h2>'+self.data_table(["Topic","2023","2024","2025"],[(n,*(f'{lookup[(n,y)]["papers"]} ({float(lookup[(n,y)]["share_of_medical_pct"]):.1f}%)' for y in (2023,2024,2025))) for n in names]))
        self.layout("research/topics/", "Medical AI Research Topics & Keywords by Year, 2023–2025", "Yearly trends in medical imaging, clinical LLMs, vision-language models, pathology, EEG, diffusion, and other medical AI topics, using transparent title rules.",
                    f'<section class="page-heading"><p class="eyebrow">Study 03 · Multi-label title analysis</p><h1>What are medical AI papers studying?</h1><p>Separate clinical domains from research methods. All years use titles and the same matching rules; abstracts are not mixed into the quantitative time series.</p></section><figure><img src="{self.url("figures/topic-trends.svg")}" alt="Medical AI domain shares by year, using multi-label title rules."></figure>{"".join(topic_tables)}<figure><img loading="lazy" src="{self.url("figures/method-trends.svg")}" alt="Yearly prevalence of segmentation, LLMs, vision-language models, diffusion, and other methods in curated medical titles."></figure><p>Multiple labels can apply to one paper, so shares do not sum to 100%. No match does not mean a topic was absent. Keyword changes use document frequency normalized by the number of medical papers in each year.</p><p><a href="{self.repo}/blob/main/reports/analysis/topics.md">Full keyword tables and interpretation ↗</a> · <a href="{self.url("data/topic_trends.csv")}">Topic CSV</a> · <a href="{self.url("data/keywords_by_year.csv")}">Yearly keywords</a></p>')

    def build(self):
        self.output.mkdir(parents=True, exist_ok=True)
        for directory in ("assets","data","figures"):
            (self.output/directory).mkdir(exist_ok=True)
        for path in (self.root/"site/assets").iterdir():
            shutil.copy2(path,self.output/"assets"/path.name)
        for path in (self.report/"figures").glob("*"):
            shutil.copy2(path,self.output/"figures"/path.name)
        for path in self.report.glob("*.csv"):
            shutil.copy2(path,self.output/"data"/path.name)
        for name in ("summary.json","submission_sources.json"):
            shutil.copy2(self.report/name,self.output/"data"/name)
        (self.output/"data/papers.json").write_text(json.dumps(self.rows,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
        self.homepage()
        for venue in sorted({r["venue"] for r in self.rows}):
            self.listing("conferences/"+slug(venue)+"/", f"{venue} Medical AI Papers, 2023–2025", [r for r in self.rows if r["venue"]==venue], "Curated medical and healthcare research, organized by conference publication year. Track details and paper-specific source links accompany each entry.")
        for year in (2023,2024,2025):
            self.listing(f"years/{year}/",f"Medical AI Conference Papers {year}",[r for r in self.rows if r["year"]==year],"Publication year follows the conference proceedings, which can differ from the arXiv submission date.")
        for topic in sorted({d for r in self.rows for d in r["domains"]}):
            self.listing("topics/"+slug(topic)+"/",topic+" Papers, 2023–2025",[r for r in self.rows if topic in r["domains"]],"This topic page uses explicit multi-label title rules. Papers can appear on more than one topic page; no match is not evidence of no relevant research.")
        self.research_pages()
        self.layout("about/","Medical AI Dataset Methodology, Sources & Citation","How this medical AI paper collection is indexed, curated, analyzed, and cited, including limitations of topic proxies and conference acceptance-rate estimates.",
                    f'<section class="page-heading"><p class="eyebrow">Sources, methods, and attribution</p><h1>A research resource you can inspect.</h1><p>We enumerate official conference catalogs before screening, keep unflagged records locally, and curate relevant medical and healthcare research. Every analysis publishes its data, rules, and denominator.</p></section><h2>Scope</h2><p>The current snapshot covers 2023–2025 and eleven conference families. It includes research papers and labeled benchmark/special tracks. It excludes workshops, student/doctoral abstracts, faculty highlights, and pure molecular research.</p><h2>Coverage and uncertainty</h2><p>The collection is not exhaustive. Pending candidates remain public, and accepted-list fallbacks and missing abstracts are documented. Medical shares are observed lower bounds in the indexed corpus. ICLR decision rates use a third-party historical submission snapshot and a consistent title proxy; they do not identify causal reviewer preferences.</p><h2>Reproduce and cite</h2><p><a href="{self.repo}/blob/main/docs/research-methodology.md">Research methodology</a> · <a href="{self.repo}/blob/main/docs/indexing.md">Indexing documentation</a> · <a href="{self.repo}/blob/main/reports/coverage.md">Coverage report</a> · <a href="{self.repo}/blob/main/CITATION.cff">Citation metadata</a></p><pre>python scripts/index_papers.py --abstracts candidates\npython scripts/fetch_submissions.py --source snapshot\npython scripts/analyze_research.py\npython scripts/build_site.py</pre><h2>Licensing</h2><p>Repository curation, code, and original analysis are dedicated under CC0. Original papers and external datasets retain their respective rights. Links and derived metadata do not transfer ownership of the underlying works.</p>')
        ns="http://www.sitemaps.org/schemas/sitemap/0.9"
        ET.register_namespace("",ns)
        tree=ET.Element("{"+ns+"}urlset")
        for url in self.urls:
            node=ET.SubElement(tree,"{"+ns+"}url")
            ET.SubElement(node,"{"+ns+"}loc").text=url
        ET.ElementTree(tree).write(self.output/"sitemap.xml",encoding="utf-8",xml_declaration=True)
        guide=f'''# Awesome Medical AI Papers

> Curated medical AI and healthcare conference papers, 2023–2025, with reproducible descriptive studies. This source guide is optional navigation, not a special ranking requirement.

- [Catalog]({self.base}): conference, year, and topic entry points.
- [Research]({self.url('research/')}): publication shares, ICLR snapshot decision rates, and title trends.
- [Methodology]({self.url('about/')}): corpus, sources, denominators, and limitations.
- [Paper metadata JSON]({self.url('data/papers.json')}): titles, summaries, source links, years, and labels.
- [Paper metadata CSV]({self.url('data/medical_papers.csv')}): derived curated-paper labels.
- [Analysis provenance]({self.url('data/summary.json')}): input hashes and aggregate results.
- [Source repository]({self.repo}): source scripts, curation ledger, citation metadata, and corrections.

Medical publication shares are lower bounds within the indexed corpus, not acceptance rates. ICLR rates are accepted/(accepted+rejected), conditional on explicit final decisions in a third-party historical snapshot. Topic labels are title proxies, not exhaustive subject annotations. Cite original paper URLs for paper claims and the repository/analysis pages for collection statistics.
'''
        (self.output/"llms.txt").write_text(guide,encoding="utf-8")
        (self.output/".nojekyll").write_text("")
        self.layout("404.html","Page Not Found","Find curated medical AI conference papers and reproducible research analyses.",f'<section class="page-heading"><h1>That page is not in the catalog.</h1><p><a href="{self.base}">Return to the medical AI paper collection ↗</a></p></section>')
        print(f"Built {len(self.urls)} HTML pages and {len(self.rows):,} paper records in {self.output}")


if __name__=="__main__":
    Site().build()
