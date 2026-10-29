"use strict";
(() => {
  const form = document.getElementById("paper-search");
  if (!form) return;
  const query = document.getElementById("query");
  const venue = document.getElementById("venue");
  const year = document.getElementById("year");
  const results = document.getElementById("search-results");
  const status = document.getElementById("result-count");
  const more = document.getElementById("show-more");
  const script = document.currentScript;
  let papers = [], limit = 30;
  const params = new URLSearchParams(location.search);
  query.value = params.get("q") || "";
  venue.value = params.get("venue") || "";
  year.value = params.get("year") || "";
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  function render() {
    const terms = query.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
    const selected = papers.filter(p => (!venue.value || p.venue === venue.value) &&
      (!year.value || String(p.year) === year.value) && terms.every(t => p.searchText.includes(t)));
    const fragment = document.createDocumentFragment();
    for (const p of selected.slice(0, limit)) {
      const article = element("article", "", "paper");
      article.append(element("div", `${p.venue} · ${p.year}`, "paper-meta"));
      const heading = element("h3");
      const link = element("a", p.title);
      link.href = p.url;
      heading.append(link);
      article.append(heading, element("p", p.summary));
      const tags = element("div", "", "tags");
      for (const method of p.methods.slice(0, 3)) tags.append(element("span", method));
      article.append(tags);
      fragment.append(article);
    }
    if (!selected.length) fragment.append(element("p", "No matching papers. Try fewer keywords or another conference."));
    results.replaceChildren(fragment);
    status.textContent = `${selected.length.toLocaleString()} matching papers · showing ${Math.min(limit, selected.length).toLocaleString()}`;
    more.hidden = selected.length <= limit;
    const state = new URLSearchParams();
    if (query.value) state.set("q", query.value);
    if (venue.value) state.set("venue", venue.value);
    if (year.value) state.set("year", year.value);
    history.replaceState(null, "", location.pathname + (state.size ? "?" + state : "") + location.hash);
  }
  form.addEventListener("submit", event => event.preventDefault());
  for (const control of [query, venue, year]) control.addEventListener("input", () => { limit = 30; render(); });
  more.addEventListener("click", () => { limit += 30; render(); });
  fetch(script.dataset.catalog).then(response => {
    if (!response.ok) throw new Error(`Catalog HTTP ${response.status}`);
    return response.json();
  }).then(data => {
    papers = data.map(p => ({...p, searchText: [p.title, p.summary, p.venue, ...p.domains, ...p.methods].join(" ").toLocaleLowerCase()}));
    render();
  }).catch(() => {
    status.textContent = "Search could not load. Browse all papers through the conference, year, and topic links.";
  });
})();
