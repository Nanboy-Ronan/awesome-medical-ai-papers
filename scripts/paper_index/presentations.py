"""Evidence-backed presentation badges, independent of paper inclusion decisions."""

import re

from .sources import clean, key, soup

LABELS = ("Oral", "Spotlight", "Highlight")
BADGE = re.compile(r" \*\*\[(?:Oral|Spotlight|Highlight)\]\*\*")


def identity(row):
    return f"{row['venue']}:{row['year']}:{key(row['title'])}"


def virtual_labels(row, venue, year):
    # Spotlights commonly have eventtype=Poster. Read the decision as well.
    decision = clean(row.get("decision") or "").casefold()
    event = clean(row.get("eventtype") or "").casefold()
    labels = set()
    for label in LABELS:
        if re.search(r"\b" + label.casefold() + r"\b", decision) or event == label.casefold():
            labels.add(label)
    # The official 2023 author guide explicitly gives these historical aliases.
    if venue == "ICLR" and year == 2023:
        if "notable-top-5%" in decision:
            labels.add("Oral")
        if "notable-top-25%" in decision:
            labels.add("Spotlight")
    return [label for label in LABELS if label in labels]


def accepted_highlights(document):
    """CVPR's accepted-paper tables mark highlights with a titled image."""
    rows = []
    for node in soup(document).select("tr"):
        title = node.select_one("td strong")
        if title:
            rows.append((clean(title.get_text(" ")), bool(node.select_one('img[title="Highlight"]'))))
    if not rows:
        raise ValueError("No accepted-paper titles found")
    return rows


def iccv_program(document):
    rows = []
    for table in soup(document).select("table.Orals, table.Posters"):
        oral = "Orals" in table.get("class", [])
        for node in table.select("tr"):
            cells = node.find_all("td", recursive=False)
            if len(cells) != 3 or not cells[2].find("small"):
                continue
            parts = []
            for child in cells[2].children:
                if getattr(child, "name", None) == "br":
                    break
                parts.append(child.get_text() if hasattr(child, "get_text") else str(child))
            rows.append((clean("".join(parts)), ["Oral"] if oral else []))
    if not rows:
        raise ValueError("No ICCV program titles found")
    return rows


def apply_badges(document, metadata):
    papers = metadata.get("papers", {})
    venue = year = None
    lines = []
    for line in document.splitlines():
        heading = re.fullmatch(r"### (.+) (20\d{2})", line)
        if heading:
            venue, year = heading[1], int(heading[2])
        match = re.match(r"(- \*\*\[(.+?)\]\(https?://[^\s)]+\)\*\*)(.*)", line)
        if match:
            row = {"venue": venue, "year": year, "title": match[2]}
            labels = papers.get(identity(row), {}).get("labels", [])
            badges = "".join(f" **[{label}]**" for label in labels)
            line = match[1] + badges + BADGE.sub("", match[3])
        lines.append(line)
    return "\n".join(lines) + "\n"
