# BD2‑Overview — Structure & Backend Review (with status)

*Original review: July 2026. Updated after the cleanup pass to record what was done and what's still open. Read this first when picking the project back up.*

---

## Where things stand

The back‑end cleanup this review called for is **essentially complete**. Data, rendering, and styling are cleanly separated; config has a single source of truth; there's data validation, a broken‑link checker, a documented build pipeline, and a reproducible local build. What remains is a little front‑end polish and a set of *optional* future features — nothing structural.

Legend: **✅ done** · **🔸 open** · **⏸ deferred by choice** · **➖ intentionally not changed**

---

## 1. The architecture (unchanged, for context)

Three layers, kept honest throughout the cleanup:

| Layer | Lives in | Holds |
|---|---|---|
| **Data** | `data/*.py`, `docs/assets/data/rapport.json` | Pure facts — stats, costs, icon paths. No HTML. |
| **Rendering** | `main.py` macros, `overrides/*.html`, `docs/javascripts/*.js` | Turns data into markup. |
| **Styling** | `docs/stylesheets/*.css` | All visual rules. |

Build pipeline order (see `CONTRIBUTING.md` for detail): `validate_data.py` → `properdocs build` → `screenshots.js` → `preview-generator.py` → `check_links.py` → deploy.

---

## 2. Concrete issues — status

**§3.1 — Python data modules were being published.** ✅ Moved `gear.py`/`icons.py`/`territory.py` to a top‑level `data/` package (no longer copied into the site); `rapport.json` moved to `docs/assets/data/`. `rapport.js` reads its path from `data-` attributes, and `rapport.md` fills them via `{{ prefix }}`.

**§3.2 — `.gitignore` gaps.** ✅ Added `__pycache__/`, `*.pyc`, `.cache/`.

**§3.3 — four near‑identical tile macros.** ✅ Extracted `_tt_header` / `_tt_cost` / `_tt_wrap` helpers; the four tile macros now share them (verified byte‑identical output).

**§3.4 — inline styles/JS inside `main.py`.** ✅ `redirect_btn` / `share_btn` now emit class‑based markup (`.redirect-btn` / `.share-btn`) with behaviour in `main.js`. Also dropped the hardcoded prefix in favour of the config value.

**§3.5 — two JS files fighting over `.local-time`.** ✅ Consolidated into a single `main.js`.

**§3.6 — dead/duplicate code.** ✅ Removed `from ast import For`, the duplicate `pymdownx.superfences`, the duplicate `elif` in `territory_tile`, and the empty `general-info/` folder.

**§3.7 — CI & dependency hygiene.** ✅ `requirements.txt` pinned with `~=`; CI uses `npm ci`; build scripts call `scripts/…`. Replaced the PR‑build idea with a local `build.ps1` / `build.sh`.

---

## 3. File structure & naming — status

- **Group build scripts.** ✅ `screenshots.js` and `preview-generator.py` moved to `scripts/` (and `screenshots.js`'s paths fixed for the new location).
- **CSS/JS naming.** ✅ `extra.css`→`main.css` (+ `slang.css` split out), `custom.js`/`extra.js`→`main.js`.
- **Convert PNG icons to AVIF/WebP.** ✅ Done for in‑page icons. ➖ Banners/social images kept as PNG on purpose — AVIF breaks Open Graph cards on Discord/Twitter.
- **`content/` vs `content-packs/`.** ➖ Kept as‑is — the split is intentional (one is a general grouping, the other an in‑game term).
- **Asset‑folder case consistency.** ✅ Tidied.

---

## 4. Clean‑backend habits — status

- **§5.1 Single source of truth for the site URL/prefix.** ✅ `main.py` derives `prefix` from `env.conf["site_url"]`; the scripts read it via `scripts/site_config.py`; `preview-generator.py` uses it instead of hardcoded domains.
- **§5.3 Data‑validation script.** ✅ `scripts/validate_data.py` checks every icon path in the data files exists; fails the build on a typo.
- **§5.4 Document the pipeline.** ✅ `CONTRIBUTING.md` written (layout, layers, local setup, pipeline order, how to add items, `[notify]` convention).
- **§5.5 Local build script.** ✅ `build.ps1` (with a `-Quick` mode that skips the Chrome screenshot step, plus a pause so the window stays open) and `build.sh`.

---

## 5. Front‑end — status

- **WIP pages leaking into the nav.** ✅ Unfinished content packs commented out of `nav:` until ready.
- **Self‑host KaTeX.** ✅ Vendored KaTeX **0.18.1** into `docs/assets/katex/` (JS, CSS, and the full `fonts/` folder); config repointed off unpkg. Along the way: fixed two content typos in `damage-formula.md` (a `\delta` inside `\text{}`, and a stray `}`) and re‑downloaded a `katex.min.js` that had been corrupted by an editor re‑save.
- **CLS — banner aspect‑ratio + hero preload.** ✅ `aspect-ratio` on `.responsive-banner`; per‑page hero preload wired into `overrides/main.html` via a `hero:` front‑matter key + `fetchpriority=high`.
- **CLS — content‑page hero `width`/`height`.** 🔸 **Still open.** The last CLS lever: add explicit dimensions to the `{: .card-header-img }` hero images at the top of content pages.
- **`theme.font: false`.** ✅ Dropped the render‑blocking Google Fonts dependency.
- **`battle.md` `!!! absract` typo.** ✅ Fixed.
- **KaTeX for trivial numbers.** ✅ Tier numerals (`I`…`EX`) converted from KaTeX to styled `.num` spans (defined once in `extra:`). Plain body‑text `$1$` — leave as a later, optional cleanup (just drop the `$…$`).
- **Tooltip positioning.** ➖ Left as‑is (it works). If it ever breaks on a theme upgrade, port the manual math to **Floating UI** rather than patching it.
- **Efficient cache lifetimes (Lighthouse).** ➖ Can't fix on GitHub Pages (fixed 10‑min `max-age`, not configurable). Only a CDN like Cloudflare in front, or a different host, would change it — low priority.

---

## 6. Future ideas (§7) — status

- **§7.1 Generate tables from the data DBs.** ✅ Built `gear_table`, `territory_table`, `crop_table`, `dish_table`, `tool_table`, `materials_table` — each rendered from its DB via a shared `_data_table` helper, so adding an item is a one‑dict edit. (Debugged: markdown‑bold in raw HTML, icon sizing vs glightbox wrapping and `max-width` clamping, list fields via `_multi`.)
- **§7.6 Broken link/image checker.** ✅ `scripts/check_links.py` scans the built site; wired in as the last build step (local + CI) so broken internal links/images fail the build.
- **§7.8 Accessibility pass.** 🔸 **Open — the recommended next thread.** Highest‑value items: the gear/territory hover tooltips are mouse‑only (keyboard/screen‑reader users can't reach that data); some coloured stat text may fail contrast; decorative icons should be `aria-hidden`.
- **§7.3 Public JSON data export.** ⏸ Parked — a cheap byproduct of the data layer, do it only when a consumer appears.
- **§7.2 Interactive calculator.** ⏸ Declined — another community tool already covers this; no wish to duplicate or split the audience.
- **§7.4 PWA / offline.** ⏸ Deferred — modest ROI (the game needs a connection anyway).
- **§7.5 Patch versioning (`mike`).** ⏸ Skipped — this is a "current state" wiki; update in place.
- **§7.7 i18n.** ⏸ Deferred — big ongoing maintenance cost; only if a language community asks and someone maintains it.

---

## 7. What's actually left

1. **Content‑page hero `width`/`height`** (§5 above) — the last CLS item, small.
2. **Accessibility pass** (§7.8) — the most worthwhile next project, especially keyboard access to the tooltips.
3. **Deferred features** — JSON export, PWA, `mike`, i18n — none are debt; pick up only on a concrete need.
4. **Content** — the half‑finished content packs are a *content* task (out of scope for this review), safely out of the nav until ready.

Nothing here is urgent, and nothing is structural. The project went from "content‑only, back‑end untended" to a cleanly‑organised, self‑validating, documented build.