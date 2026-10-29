# Discovery, citation, and sustainable repository growth

The catalog's purpose is to help researchers find useful papers and verify
claims. Discovery improvements support that work; they do not guarantee search
rankings, inclusion in AI answers, or GitHub stars.

## Implemented

- A GitHub Pages catalog with static conference, year, and topic pages. Every
  paper is reachable through ordinary HTML links, even without JavaScript.
- Client-side search over titles, summaries, venues, and research labels, with
  shareable query/filter URLs. No search service or account is needed.
- Original research reports, CSV downloads, source provenance, and methodology
  pages that distinguish publication shares from submission decision rates.
- Unique titles/descriptions, self-canonical URLs, sitemap, social sharing image,
  Open Graph/Twitter metadata, and visible source/citation links.
- Dataset structured data describing the visible collection and downloadable
  metadata; original paper claims link to the authors' own sources.
- An optional `llms.txt` navigation guide, citation metadata, and paper/correction
  issue templates. The guide is a source map, not a special ranking mechanism.
- Repository topics and a descriptive About field, plus a website link once the
  site is live. The configuration is in `config/site.json`.

Google's [AI feature guidance](https://developers.google.com/search/docs/appearance/ai-features)
uses normal SEO fundamentals: crawlable pages, helpful visible text, internal
links, and structured data consistent with the page. It does not require a
special AI text file. GitHub's [topic documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
explains how topics support repository discovery.

## Build and publish

```sh
python -m pip install -r requirements-index.txt
python scripts/build_site.py
```

The builder consumes README and committed analysis outputs; it does not need
the ignored full index or a network crawl. It rejects an analysis corpus that
no longer matches the paper list. Generated HTML lives in ignored `_site/`.
The Pages workflow builds and deploys the site after pushes to `main`. The
repository's Pages source is GitHub Actions; the standard `github-pages`
deployment environment is used.

Update the analysis after changing paper records, and update `config/site.json`
if the canonical site URL changes. The project is hosted under a subpath, so a
project-level `robots.txt` would not control crawling of the host. The sitemap
is linked from the site footer; no ineffective project-level robots file is
present. See Google's [robots location rules](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt).

## Measure useful outcomes

Use GitHub traffic and referrers, stars/forks, contribution quality, and incoming
citations to assess whether people find the resource useful. Website search
clicks and CSV downloads are useful engagement signals if analytics are added
later with appropriate disclosure. Do not treat a star count as research quality.

The owner can verify the public site in Google Search Console and submit its
sitemap to inspect indexing and search queries. This needs the owner's Search
Console account; no verification is claimed here. Repository social previews
can use `site/assets/social-card.png` through GitHub Settings if desired.

Sharing the original research findings with transparent caveats can attract
relevant readers. No automated promotional messages, unsolicited issue/PR spam,
paid stars, or fabricated popularity metrics are part of this workflow.
