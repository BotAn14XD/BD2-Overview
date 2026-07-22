# BD2‑Overview — Second Back‑End Review + `main.css` Audit

*Follow‑up pass, July 2026. The first review (`BACKEND-REVIEW.md`) did the heavy structural cleanup — three‑layer separation, single‑source config, data validation, link checker, documented build. This pass assumes all of that and looks for what's **left**: optimization wins, correctness bugs, and the state of the stylesheet. Nothing here overlaps the first review's open items (hero `width`/`height`, accessibility pass, deferred features), and nothing here is "write more content."*

Legend: **🔴 bug / correctness** · **🟠 optimization** · **🟡 maintainability** · **🟢 nice‑to‑have**

---

## Part 1 — Fresh back‑end / optimization findings

### 1.1 🔴 The `!!! absract` typo is still live in `battle.md`

The first review recorded this as **✅ Fixed**, but `docs/mechanics/battle.md:27` still reads `!!! absract "Grid System …"`. Because `absract` isn't a registered admonition type, Material renders it as a **generic, un‑iconed, default‑bordered** box instead of the intended "abstract" style — so that whole Grid‑System block looks visually broken next to the correctly‑spelled `!!! abstract` blocks right below it (lines 36, 67, 120). There's also a separate spelling slip at line 180, `!!! abstract "Targetting Lines"` (double‑t in the *title* text — cosmetic, not a render bug, but worth catching in the same sweep). Fix line 27 to `abstract`. This is the single highest‑value one‑character change on the site.

### 1.2 🟠 Large content PNGs were never converted

The first review closed "convert PNG → AVIF/WebP" as done *for in‑page icons*, and deliberately kept **banners/social images** as PNG for Open Graph compatibility. That reasoning is sound, but it left a gap: full **illustration** PNGs that are neither icons nor OG banners. The worst offender is `assets/images/damage-formula/fight_1.png` at **3.6 MB** — a single in‑content image larger than the entire rest of a typical page. `assets/images/faq/12-pick.png` (542 KB) is a second case. These load inline in the article body, not as share cards, so the OG‑card argument doesn't apply to them. Converting just `fight_1.png` to AVIF would likely save 3+ MB on the damage‑formula page (already the heaviest page on the site at 104 KB of markup). Recommendation: add a cheap guard to `scripts/validate_data.py` (or a new `scripts/check_assets.py`) that **fails the build if any file under `docs/assets/images/` that isn't in `site-assets/` exceeds ~400 KB**, so a heavy PNG can never silently ship again.

### 1.3 🟠 KaTeX and the whole font folder ship uncompressed and unversioned

Self‑hosting KaTeX 0.18.1 (first review) was the right call for reliability, but three follow‑ups:
- The **`fonts/` folder** is the bulk of KaTeX's weight and every page that renders a formula pulls several font files. Confirm the build only ships the font *formats* you need (WOFF2 is enough for all current browsers; the legacy `.woff`/`.ttf`/`.eot` variants in the KaTeX bundle can be deleted, cutting that folder substantially).
- `katex.min.js` + `auto-render.min.js` are loaded on **every page** via `extra_javascript`, including pages with no math at all (index, slang, territory, rapport…). Since `arithmatex: generic` defers rendering to the auto‑render pass, you could gate the KaTeX includes to only the two pages that actually use math (`battle.md`, `damage-formula.md`) via per‑page `extra_javascript` front‑matter or a template conditional in `overrides/main.html`. That removes a render step and ~three requests from the majority of pageviews.
- The corrupted‑`katex.min.js` incident noted in the first review is a symptom of vendoring binaries into git with no integrity check. Add the file's expected SHA‑256 to `validate_data.py` so a bad re‑save fails the build instead of shipping.

### 1.4 🟡 `preview-generator.py` re‑implements HTML parsing with regex

`scripts/preview-generator.py` pulls slang terms out of the built HTML with `re.findall(r'<li\s+class="slang-item"…')` and strips tags with `re.sub(r'<[^>]+>', '', …)`. This works today but is brittle: it silently breaks the moment the slang template markup changes (a wrapping element, an attribute reorder, a multi‑`<p>` definition). The `check_links.py` script already imports `html.parser.HTMLParser` — reuse that same approach here so both scripts parse HTML the same, robust way. The `surgically_fix_faq_meta()` function is a second instance of the same smell: it rewrites `<meta>` tags in built HTML with three chained regexes. The cleaner fix is to emit the correct FAQ meta at **build time** via the `hero`/`image` front‑matter mechanism you already built in `overrides/main.html`, and delete the post‑build surgery entirely.

### 1.5 🟠 The screenshot step is the slowest, most fragile part of the pipeline — and mostly redundant work

`scripts/screenshots.js` launches headless Chrome and screenshots **every** `.slang-item` on every build. With a 199 KB slang page that's a lot of elements, re‑rendered from scratch each deploy even when only one term changed. Two improvements: (a) skip terms whose `share-assets/<slug>.png` already exists **and** whose source is unchanged (hash the term block), turning a full re‑shoot into an incremental one; (b) since this is the only reason Chrome/puppeteer is a build dependency at all, gating it behind "did the slang page change?" would let most deploys skip Chrome entirely. This is the difference between a ~10‑second deploy and a multi‑minute one.

### 1.6 🟡 `main.py` — the `IMAGES` macro loop shadows a builtin and skips escaping

Two small things in `main.py`:
- The `for key, info in IMAGES.items()` block (line 162) builds an `<img>` with `title="{label}" alt="{label}"` by raw f‑string. If any label ever contains a `"` or `<`, it breaks the tag. `rapport.js` already has a careful `esc()` helper for exactly this reason — the Python side should have the equivalent (`html.escape`) on `label`, `name`, and `desc` fields that originate from data. Low probability today, but it's an injection‑shaped hole in the one place data becomes markup.
- `time` is defined both as a **macro** (line 89) and as a local variable inside `territory_tile`/`crop_tile` (`time = item.get("time")`). It's harmless because of scoping, but shadowing your own macro name is a readability trap; rename the locals to `build_time`.

### 1.7 🟢 Build‑pipeline resilience

- `build.sh` uses `set -euo pipefail` (good) but `build.ps1` swallows failures into a `catch` that just prints and then hits `finally`/`Read-Host` — so a **double‑clicked** run that fails still exits 0 from CI's perspective if anyone ever wires it up. Keep the pause for humans, but `exit 1` inside the `catch` so it can't be mistaken for success in automation.
- Consider caching `pip`/`npm` and the KaTeX fonts in the GitHub Actions workflow (`actions/setup-python` cache + `~/.cache`) to shave install time off every deploy.

### 1.8 🟢 Metadata / SEO plumbing

- `properdocs.yml` sets `social.cards: false`, so the `social` plugin is installed but producing nothing — every page's OG image falls back to the static `banner.png` via `overrides/main.html`. That's a deliberate choice (the first review notes AVIF/OG friction), but since cards are off, the `social:` plugin block and its `cards_layout_options` are dead config; either turn cards on for the pages that would benefit or drop the block to a bare `- social` (or remove it) to stop paying its build cost.
- There's no `robots.txt` shipped and the sitemap is hand‑patched by `preview-generator.py`. That works, but a `robots.txt` pointing at the sitemap is a 2‑line SEO freebie.

---

## Part 2 — `main.css` audit

You called this "the messiest place," and the structure bears that out: it's ~1,120 lines carrying **117 `!important` declarations** and several duplicated selectors. It's not broken — but it's the file most likely to bite you on the next theme upgrade. Findings, roughly in priority order:

### 2.1 🔴 Duplicate selectors with conflicting rules

Genuine duplicates, verified by line number:
- **`.card-header-img`** is defined **twice** — lines 466–474 (index‑card version, everything `!important`) and 593–599 (nav‑card version, no `!important`). They set overlapping properties (`object-position`, `width`, `height`) with different values. Whichever loses the cascade is invisible to you until a card renders wrong. These are two *different* visual roles wearing one class name — split them (`.index-card-img` vs `.nav-card-img`) so they can't collide.
- **`table.data-table`** — lines 312 and 333. Trivially mergeable into one block.
- **`.gear-name`** — lines 634 and 724, plus the modifier rules. Consolidate.
- **`.tooltip-line.white`** — declared **three** times (683, 715, 717), all setting the same color. Delete two.

### 2.2 🔴 The `!important` epidemic

117 `!important`s in one file is the headline problem. Most exist to out‑shout the Material theme's own specificity, which is understandable, but the current approach is "add `!important` until it works," and that ratchets — every future rule now *also* needs `!important` to override these. Two structural fixes:
- **Raise specificity instead of forcing.** Material scopes almost everything under `.md-typeset`. A rule written as `.md-typeset .data-table td` beats a bare theme rule *without* `!important`. Prefixing your component selectors with `.md-typeset` (which you already do inconsistently — some rules have it, some don't) removes the need for the majority of these.
- **The index‑card scaffolding (lines 442–539) is the worst cluster** — nearly every line is `!important` because it's fighting the theme's `.grid.cards` layout via deep descendant selectors like `.grid.cards.center-content > ul > li > p:first-of-type`. This is extremely fragile: it depends on the *exact* DOM order Material emits (first `<p>`, the `<hr>`, second `<p>`). A Material update that adds a wrapper element silently destroys every card. Strong recommendation: stop styling by DOM position and instead give the card pieces real classes in the markdown/macro (you already control the card HTML in `index.md`), then style those classes. That single change would delete most of the `!important`s in the file.

### 2.3 🟡 Dead / orphaned rules

- `.md-banner { display: none }` (line 385) hides the survey banner entirely, but `main.js`'s `manageSurveyBanner()` flips it back to `block`. So the survey system is styled in three places (`.md-banner`, `.survey-announce-bar`, the JS) with the CSS default being "off." Worth a comment block explaining the on/off dance, or it reads as a bug.
- `.gear-tooltip-box.flipped-down::before` (line 746) styles a `::before` arrow, but I don't see the base `::before` triangle defined anywhere — if the arrow was removed during the tooltip rework, this rule and its `flipped-down` sibling are orphaned. Verify the tooltip still has a pointer; if not, delete.
- `.toc-only { display: none }` and `.no-bullets`/`.no-bullets ul li` — confirm these classes are still used in any `.md`; grep turned them up only in CSS in the files I sampled.

### 2.4 🟡 Organization & de‑duplication

- The file is one flat list with `/* SECTION */` comments. It would read far better split by concern — and since `extra_css` already loads three sheets (`main`, `rapport`, `slang`), the precedent for splitting exists. At minimum, pull the **survey** block (lines ~381–435 and 865–1019, ~200 lines) into its own `survey.css` loaded only where needed; it's a self‑contained subsystem that has no business in the global sheet.
- **Magic colors are repeated as literals.** `#ffe8aa` (the yellow) appears in the `.yellow` class, the tooltip header, the data‑table header, and inline in `main.py`. `#1a1f2c` (tooltip bg) and `#374151` (borders) likewise recur. Promote the recurring palette to `:root` custom properties (`--bd-gold`, `--bd-tooltip-bg`, `--bd-border`) at the top and reference them. One edit re‑themes the site, and it kills a class of "I changed the yellow in four places but missed the fifth" bugs.
- `.icon` uses `transform: scale(1.5)` on top of `height: 1.2em` (line 14). Scaling for sizing means the element's *layout* box (1.2em) differs from its *painted* size (1.8em), which causes overlap and mis‑alignment against surrounding text and is almost certainly behind any icon‑spacing fiddliness. Prefer setting the real `height`/`width` and dropping the transform.

### 2.5 🟢 Small correctness nits

- Line 168: `display: flex-start !important` — `flex-start` is **not a valid value for `display`** (it's a value for `justify-content`/`align-items`). This declaration is ignored by every browser; either it's dead or it was meant to be a flex property on a different line. Clean it up.
- `.md-typeset .q-misc > .admonition-title` (line 248) sets `background-color: rgba(13, 148, 136, 0.1)` — a **teal**, while its border and icon are `#4A5568` **slate**. Almost certainly a copy‑paste leftover from another admonition; the title tint doesn't match the accent.
- Several rules mix `px`, `em`, and `rem` for the same visual dimension (icons in `em`, tooltips in `rem`, tiles in `px`). Not a bug, but standardizing tooltip/tile sizing on `rem` would make the whole component scale cleanly with the user's font‑size setting.

---

## Suggested order of attack

1. **`battle.md:27` `absract` typo** — 30 seconds, visibly fixes a broken box. (§1.1)
2. **Convert `fight_1.png`** (and add the asset‑size build guard). — biggest single byte win. (§1.2)
3. **De‑duplicate the four conflicting CSS selectors.** — removes latent render bugs. (§2.1)
4. **Re‑class the index cards** to kill the positional `!important` cluster. — the real CSS debt. (§2.2)
5. Everything else is incremental polish; pick up opportunistically.

None of this is urgent and none of it is structural — the first review already did the structural work. This is the "sand off the rough edges and stop the theme upgrade from hurting" layer.
