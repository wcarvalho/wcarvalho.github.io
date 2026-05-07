---
name: update-publications
description: Add new publications to main-pages/publications.md on Wilka's site. Triggered by "/update-publications", "add publications", "add these papers to my pubs page", or pastes of Google Scholar listings / arXiv IDs in the context of this site. Reads existing entries to reuse author hyperlinks; writes HTML blocks matching the existing format; verifies via `bundle exec jekyll serve`.
---

# update-publications

Adds new publication entries to `main-pages/publications.md`. The page is hand-written HTML blocks (not jekyll-scholar / BibTeX). This skill matches the existing format exactly and reuses author URLs already on the page.

## Behavioral conditionals

Follow these rules in order. They are conditionals, not aspirations.

### 1. Input phase

- When invoked without input → ask: "Paste arXiv IDs/URLs or the Scholar listing for the pubs to add."
- When the user pastes text → auto-detect:
  - arXiv IDs match `\b\d{4}\.\d{4,5}\b`
  - arXiv URLs match `arxiv\.org/abs/\d{4}\.\d{4,5}`
  - Free-form Scholar text otherwise (one block per pub)
- For each detected arXiv ID → WebFetch `https://arxiv.org/abs/<id>` to get authoritative title + author list.
- For non-arXiv pubs (e.g., Neural Computation) → parse the user-pasted text. DO NOT fetch external URLs unless the user supplies one.

### 2. Author-URL reuse — grep, do not invent

For each author name in each pub:

1. Grep `main-pages/publications.md` for the author's full name and last name (case-insensitive). The pattern to look for is `>([Author Name])</a>` — the surrounding `<a href="...">` gives you the URL to reuse.
2. When found → reuse the existing `<a href="...">` URL exactly.
3. When not found → render the name as plain text. **DO NOT invent a URL.** Even a plausible guess (e.g., a `*.github.io` page) is forbidden. Bare text is the safe default.
4. For "Wilka Carvalho" / "W Carvalho" → ALWAYS render as:
   ```html
   <a href="/"><span style="color: #9f30a5">Wilka Carvalho</span></a>
   ```

When the user pastes initials-only authors (e.g., "SJ Gershman"), expand to the full name found in publications.md before grepping (e.g., "Samuel J Gershman" if present, or fall back to the form on the page).

### 3. Duplicate check — do not skip

For each pub, before generating any HTML:

- Grep `main-pages/publications.md` for the arXiv ID (e.g., `2508.15693`).
- Grep for the first 5–8 distinctive words of the title (case-insensitive).
- When either matches → skip that pub and report "already on page" to the user. Do not insert a duplicate.

### 4. Pre-write summary — show, then ask

Before generating any HTML, present a summary table to the user (one row per pub):

| # | Title | Authors (linked / bare) | Venue | Year | Dup? | Image? |
|---|-------|-------------------------|-------|------|------|--------|

For the Authors column, mark each author with `[linked]` (URL reused from publications.md) or `[bare]` (will render as plain text). Example:
```
W Carvalho [wilka], A Lampinen [linked: lampinen.github.io], H Lee [bare]
```

Then ask: "Confirm authors / venue / year, and provide image paths."

**DO NOT generate HTML until the user confirms.**

### 5. Image prompt — per pub

For each confirmed pub, ask: "Image path for `<title>` (or 'skip')?"

- When the user provides a path → use the **with-image** template.
- When the user says "skip" / "none" → use the **no-image** template (col-sm-9 instead of col-sm-2 + col-sm-7).
- Image paths should be relative to the site root (e.g., `/publications/nicewebrl/figure.png`). Strip leading `./` if present.

### 6. HTML generation

Use these templates exactly. Match indentation.

**With image:**
```html
<!-- {{TITLE_SHORT}}, {{VENUE}} {{YEAR}} -->
<div class="row publication">
<div class="col-sm-2 center">
  <img class="pub-image responsive" src="{{ site.baseurl }}{{IMAGE_PATH}}">
</div>
<div class="col-sm-7 center">
  <p>
  <strong>
    <a href="{{LINK_URL}}">{{TITLE}}</a>
  </strong>
  <br>
  {{AUTHOR_LIST}}
  <br>
  <em> {{VENUE}}, </em> {{YEAR}} <br>
  </p>
</div>
</div>
```

**Without image:**
```html
<!-- {{TITLE_SHORT}}, {{VENUE}} {{YEAR}} -->
<div class="row publication">
<div class="col-sm-9 center">
  <p>
  <strong>
    <a href="{{LINK_URL}}">{{TITLE}}</a>
  </strong>
  <br>
  {{AUTHOR_LIST}}
  <br>
  <em> {{VENUE}}, </em> {{YEAR}} <br>
  </p>
</div>
</div>
```

**Author list formatting:**
- Comma-and-newline-separated, one author per line, indented two spaces.
- Linked: `<a href="{URL}">{Name}</a>`
- Bare: `{Name}` (no tag)
- Wilka: `<a href="/"><span style="color: #9f30a5">Wilka Carvalho</span></a>`
- The last author has no trailing comma.

Example:
```html
  <a href="/"><span style="color: #9f30a5">Wilka Carvalho</span></a>,
  <a href="https://lampinen.github.io/">Andrew Lampinen</a>
```

**Venue formatting:**
- Published journal/conf → `<em> {Venue}, </em> {Year}` (e.g., `<em> Neural Computation, </em> 2024`, `<em> ICML, </em> 2025`)
- Under review → `<em> Under review at {Venue}, </em> {Year}`
- No peer-reviewed venue / preprint only → `<em> Preprint, </em> {Year}` — short and clean.
- Honors / orals → append `<span style="color: red">(Oral)</span>` (or `(Spotlight)`, etc.) AFTER the year on the same line. Example: `<em> ICML, </em> 2025 <span style="color: red">(Oral)</span>`.

**DO NOT** ever write `arXiv preprint arXiv:<id>, <year>` in the venue line. The arxiv URL belongs on the **title link** only (via `<a href="https://arxiv.org/abs/<id>">{title}</a>`); duplicating the ID below is ugly. The reader clicks the title to reach arxiv.

**DO NOT** add a secondary arxiv-preprint line below a primary venue. If a paper has a real venue (or "Under review at X"), that's the only venue line — no need to also say "arXiv preprint arXiv:X". The title link already conveys "this is on arxiv."

**Multiple venues** (e.g., conference + workshop where the paper was presented at both): stack `<em>...</em>` lines separated by `<br>`. Primary venue first. The last venue line has no trailing `<br>`. Example:
```html
<em> ICLR, </em> 2023 <br>
<em> NeurIPS Deep RL Workshop, </em> 2022
```

**Pub-link buttons** (Website, Code, arXiv, Talk, Podcast, etc.): when the user supplies a website or code URL, append a `pub-links` block AFTER the closing `</p>` of the main paragraph but INSIDE the `col-sm-7` div. Use one `<a><button>...</button></a>` per link. Pattern:
```html
  <div class="row pub-links">
  <p>
    <a href="{{WEBSITE_URL}}">
    <button type = "button" class = "btn btn-primary">
    Website
    </button>
    </a>
    <a href="{{CODE_URL}}">
    <button type = "button" class = "btn btn-primary">
    Code
    </button>
    </a>
  </p>
  </div>
```
Always ask the user for website/code URLs when adding a pub. If they don't have any, skip the block.

**Insertion location:**
- Insert all new entries at the top of `<div class="publications">` — that is, **immediately after the line `<div class="publications">`** in `main-pages/publications.md` (around line 15–16).
- Order new entries newest-first.
- Separate entries with one blank line.

**LINK_URL choice:**
- Prefer arXiv abs URL for preprints: `https://arxiv.org/abs/<id>`.
- For published papers, prefer DOI or publisher URL if the user supplies one; otherwise arXiv abs URL.
- If no URL is available, omit the `<a>` tag around the title — render `<strong>{{TITLE}}</strong>` plain.

### 7. Verification — do not skip

After writing the HTML edits:

1. **Check if a jekyll is already running on port 4000** with `lsof -i :4000`.
   - If yes and it was started with `--no-watch` (check `ps aux | grep jekyll`) → run `bundle exec jekyll build` from the repo root. The existing serve will pick up the rebuilt `_site/` automatically.
   - If yes and it has `--watch` (or no flag) → just edit the file; auto-regen will rebuild.
   - If no jekyll is running → start one: `bundle exec jekyll serve` with `run_in_background: true`. Wait for the "Server address" line, then report the localhost URL.
2. **When jekyll errors** → show the error to the user and revert the edit (or offer to revert). Do NOT claim success.
3. **When jekyll builds clean** → tell the user: "Preview at http://127.0.0.1:4000/main-pages/publications/ — new entries are at the top of Publications."

If `bundle` is not installed or fails: surface the error verbatim, suggest `bundle install`, and stop.

## DO NOT rules (recap)

- **DO NOT** invent author URLs. Grep publications.md or render bare.
- **DO NOT** write `arXiv preprint arXiv:<id>` in the venue line. Use `Preprint, <year>` for unrefereed work; the arxiv URL goes on the title link only.
- **DO NOT** add `<img>` blocks unless the user provides a path.
- **DO NOT** skip the duplicate check.
- **DO NOT** write HTML before the user confirms the parsed summary table.
- **DO NOT** skip the jekyll-serve verification step.
- **DO NOT** reorder or edit existing entries — only insert new ones.
- **DO NOT** uncomment the Preprints section. New preprints go at the top of Publications alongside published papers.

## Notes on the page format

- File: `main-pages/publications.md` (Jekyll renders to `/main-pages/publications/`).
- Layout: `default`. Title: "Publications".
- Each pub is a `<div class="row publication">`. Bootstrap-like grid (col-sm-2 image + col-sm-7 text, or col-sm-9 text-only).
- Image refs use `{{ site.baseurl }}` prefix.
- Wilka's name is always wrapped in a purple `<span style="color: #9f30a5">`.
- Authors are linked to their personal websites when known. The page is its own author-URL registry — grep before adding.

## Common author URLs already on the page (as of 2026-05)

This is a hint, not a database. Always grep to confirm:

- Andrew Lampinen → `https://lampinen.github.io/`
- Honglak Lee → `https://web.eecs.umich.edu/~honglak/`
- Satinder Singh → `https://web.eecs.umich.edu/~baveja/`
- Richard L. Lewis → `http://www-personal.umich.edu/~rickl/`
- Angelos Filos → `https://oatml.cs.ox.ac.uk/members/angelos_filos/`
- Felix Hill → `https://fh295.github.io/`
- Murray Shanahan → `https://www.doc.ic.ac.uk/~mpsha/`

If an author you need is not on the page yet, render them bare and let the user add a link manually later.
