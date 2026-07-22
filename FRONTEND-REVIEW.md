# BD2‑Overview — Front‑End & Content Review

*July 2026. This is the front‑end counterpart to the back‑end reviews. Part 1 looks at the **content itself** — how it reads, how it's structured, how a new player moves through it. Part 2 is a set of **website improvements** that are deliberately **not** in `BACKEND-REVIEW.md` and are **not** "write more pages" — they're ways to make the content you already have work harder.*

Legend: **🔴 fix** · **🟠 worth doing** · **🟢 polish**

---

## Part 1 — Content review

The writing is genuinely good: the tone is confident, the TL;DR admonitions are excellent onboarding, and the "preferred vs standard answer" framing on the rapport page is the kind of thing a new player actually needs. The issues below are about consistency and findability, not quality.

### 1.1 🔴 Proofreading pass on the mechanics pages

A few concrete slips found while sampling (there are almost certainly more — these justify a full pass):
- `battle.md:27` — `!!! absract` renders as a broken, un‑styled box (also flagged in the back‑end review; it's a content‑visible bug so it belongs here too).
- `battle.md:180` — "Targetting Lines" (double‑t). Also "Targetting" vs "Targeting" is used inconsistently across the page — pick one (US "Targeting").
- General: the prose has occasional dropped articles ("you have ability to position" → "the ability to"; "in which you have ability to use" → "you can use"). A single read‑through with a grammar checker would lift the polish noticeably, especially on `index.md` and `battle.md`, which are the first two pages every visitor sees.

Recommendation: run the top‑of‑funnel pages (`index`, `battle`, `damage-formula`, `FAQ`) through a spell/grammar checker once. These four pages carry the first impression; the deeper reference pages matter less.

### 1.2 🟠 Reading length and the "wall of admonitions" pattern

`damage-formula.md` is **104 KB** of markup and `slang.md` is **199 KB** — these are enormous single pages. The damage‑formula page in particular is the heaviest thing on the site and leans hard on stacked admonitions and KaTeX. Two content‑level responses:
- **Add an in‑page "On this page" mini‑TOC** at the top of the long reference pages (battle, damage‑formula, gear, territory). Material supports `toc.integrate` or a right‑rail TOC; a new player landing mid‑page from a search result has no sense of where they are in a 100 KB document.
- **The nested‑admonition style** (abstract → warning → image, three levels deep in `battle.md`) is powerful but can bury key facts. Consider promoting the one‑line "what you actually need to know" out of the collapsed block and leaving the detail inside. The rapport page's `!!! tip "TL;DR"` pattern is the model — replicate that at the top of every long page.

### 1.3 🟠 Terminology consistency between pages

The site uses a lot of game jargon (Costume, Companion tab, Very Front, Vault, Rapport, Potential Liberation). The **slang glossary already exists and has a share/anchor system** (`?term=…`) — but the mechanics pages mostly don't link into it. First use of a jargon term on any page should link to its glossary entry. You've built the cross‑linking infrastructure (`.cross-link`, the `?term=` deep links, the whole `preview-generator.py` proxy‑route system); the content just isn't taking advantage of it yet. This is high leverage because it's reusing something you already engineered.

### 1.4 🟠 The index page is a link hub, not an on‑ramp

`index.md` is essentially a grid of cards linking everywhere — which is fine as a directory, but a first‑time visitor with no BD2 knowledge has no suggested path. Consider a short **"New here? Start with these three"** row at the very top (Battle System → Gear → FAQ, say), visually distinct from the exhaustive card grid below. The cards are comprehensive but flat; there's no signal about *what to read first*. This is a re‑ordering/framing change, not new content.

### 1.5 🟢 Content freshness signals

You already run `git-revision-date-localized`, so pages show a last‑updated date — good. But a live game wiki also benefits from a visible **"current as of patch X"** marker on volatile pages (events, banners, content packs), since "updated 3 months ago" reads as stale even when the mechanics are still correct. A tiny front‑matter `patch:` value surfaced in the template would let readers trust older‑dated pages.

### 1.6 🟢 Commented‑out nav is a content‑visibility question

`properdocs.yml` has five content packs commented out of the nav (Path of Adventure, Last Night, Glupy Diner, Golden Colosseum, Fantasia Square) — and `last-night.md` is already **19.5 KB** of written content, `path-of-adventure.md` 3.3 KB. That's substantial finished work that's invisible to users. Not asking you to write more — asking whether some of what's *already written* is complete enough to unhide. A "🚧 Draft" badge on a page is often better than the page not existing at all for SEO and for players who'd rather have 80% than nothing.

---

## Part 2 — Website improvements (excluding back‑end‑review items and excluding "more content")

These are additive front‑end/UX improvements. None of them appear in `BACKEND-REVIEW.md`'s open list (which is: hero `width`/`height`, the accessibility pass, and the deferred features JSON/PWA/mike/i18n), and none of them are "write more pages."

### 2.1 🟠 A site‑wide search‑result experience beyond the theme default

Material's built‑in search is fine, but you have three *custom* search UIs already (the slang filter, the rapport autocomplete, the theme search) that don't know about each other. Unifying discovery — e.g. making the main search surface glossary terms and rapport costumes as first‑class results — would make the site feel like one tool instead of three. Even just documenting the `?term=` deep‑link scheme in the search hints would help.

### 2.2 🟠 "Copy share link" and anchor UX, extended

You built a nice `share_btn` macro + clipboard JS. Two extensions that cost little:
- Add a **"back to top"** floating button on the long pages (damage‑formula, slang, territory) — pure CSS/tiny JS, big usability gain on 100 KB+ pages.
- Make section headings themselves clickable anchors with a hover‑visible `#` link (Material has `permalink: true` for `toc` — you set `separator` but not `permalink`). This is the conventional wiki behavior and pairs naturally with the share button you already have.

### 2.3 🟠 Light‑mode / palette toggle

`properdocs.yml` hard‑pins `scheme: slate` (dark only) with no `toggle`. A lot of the custom CSS assumes a dark background (hard‑coded `#1a1f2c` tooltip backgrounds, white text). Offering a light scheme is real work *because* of that hard‑coding — but even if you don't ship light mode, wiring the palette **toggle** with just a second dark‑variant, or at minimum respecting `prefers-color-scheme` for the *browser chrome*, is a courtesy. If you do want light mode eventually, the `:root` custom‑property refactor recommended in the CSS audit is the prerequisite that makes it feasible.

### 2.4 🟠 Keyboard & focus states for the custom interactive bits

This overlaps the accessibility pass the back‑end review already flagged, so I'll keep it to the *front‑end‑specific* slice not covered there: the survey radio boxes, the slang quick‑filter buttons, and the rapport autocomplete need **visible `:focus-visible` outlines**. The rapport JS already implements full arrow‑key/Enter/Escape handling (nicely done) — but the CSS `:focus` styling for the options is `aria-selected`‑based, which won't show for keyboard‑Tab users who haven't opened the list. A `:focus-visible` ring on every custom control is a small, self‑contained CSS addition.

### 2.5 🟢 Motion & performance felt‑experience

- Several hover transitions (`transition: all 0.2s`) animate `all`, which forces the browser to watch every property. Narrow them to the properties that actually change (`transition: background-color 0.2s, border-color 0.2s`). Cheaper and smoother, and you already do it correctly in `rapport.css` — just apply the same discipline in `main.css`.
- The `rapport.css` `@media (prefers-reduced-motion: reduce)` block is a great touch — extend that same courtesy to the gallery hover‑zoom and card transitions in `main.css`, which currently animate regardless of the user's motion preference.

### 2.6 🟢 Print / offline‑read stylesheet

A one‑screen `@media print` block (hide nav/sidebar/search, expand collapsed admonitions, black‑on‑white text) turns any page into a clean printable/PDF‑able reference. For a game guide people genuinely do want to print builds and formula sheets. This is *not* the PWA/offline feature the back‑end review deferred — it's a dozen lines of CSS.

### 2.7 🟢 Structured data for the FAQ

`FAQ.md` is 19 KB of question/answer content, and you already do custom OG‑meta surgery for it. Adding **`FAQPage` JSON‑LD** structured data would make those Q&As eligible for rich results in Google search. It's a template/front‑matter addition, generated from the same headings, and it's exactly the kind of SEO win that a well‑structured FAQ page is built for.

---

## Priority shortlist

If you only touch a handful:
1. **Proofread the four top‑of‑funnel pages** (§1.1) — first impressions.
2. **Link jargon into the glossary you already built** (§1.3) — reuses existing infrastructure.
3. **Add `permalink` anchors + a back‑to‑top button** (§2.2) — cheap, expected wiki UX.
4. **`:focus-visible` rings on the custom controls** (§2.4) — accessibility with a small surface.
5. **Unhide the drafts that are actually finished** (§1.6) — recover buried work.

The content is strong; most of the gap is in *navigation, findability, and consistency* rather than in what's written. The interactive components (rapport search, slang filter, tooltips) are the standout front‑end work already — the goal now is to make the static pages feel as considered as those do.
