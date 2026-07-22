# Maintaining the Tactical Compendium

A short reference for how this site is built and how to work on it, so the
non-obvious pieces aren't only in your head. If you're returning after a
break, read this first.

## What this is

A static documentation site for **Brown Dust II**, built with
[Properdocs](https://github.com/) (a fork of MkDocs, using the Material
theme). You write Markdown; the build turns it into the static `site/`
folder, which is deployed to GitHub Pages.

## Repository layout

| Path | What it is | Edit it? |
|---|---|---|
| `docs/` | All site content: Markdown, images, CSS, JS. | **Yes** — this is where you work. |
| `data/` | Python data files (gear, icons, territory). The facts behind the tooltips. | **Yes** — add game data here. |
| `scripts/` | Post-build tooling (screenshots, share-page generator, data validator). | Occasionally. |
| `main.py` | The macros: Python functions that inject HTML (tooltips, tiles, buttons) into Markdown. | Occasionally. |
| `overrides/` | Theme template overrides (`main.html`, `404.html`). | Occasionally. |
| `properdocs.yml` | Site config: nav, plugins, theme, `site_url`. | Yes. |
| `site/` | **Generated output.** | **No — never edit by hand.** It's rebuilt every deploy. |

## The three layers

Keeping these separate is what keeps the project maintainable:

- **Data** — `data/*.py`, `docs/assets/data/rapport.json`. Pure facts. No HTML.
- **Rendering** — `main.py` macros, `overrides/*.html`, `docs/javascripts/*.js`. Turns data into markup.
- **Styling** — `docs/stylesheets/*.css`. All visual rules.

When you catch yourself putting HTML in a data file, or a color in a macro,
push it down a layer.

## Working locally

One-time setup:

```
pip install -r requirements.txt
npm ci
```

Live preview while editing (auto-reloads):

```
properdocs serve
```

Full production build (mirrors the deploy — run this before pushing):

```
./build.ps1        # Windows (PowerShell)
./build.sh         # macOS / Linux / Git Bash
```

## The build pipeline

The GitHub Actions workflow (`.github/workflows/publish.yml`) runs these
steps in order on every push to `main`. The local build scripts do the same:

1. **`python scripts/validate_data.py`** — checks every icon path in the data files actually exists. Fails fast on a typo.
2. **`properdocs build`** — Markdown + macros → `site/`.
3. **`node scripts/screenshots.js`** — screenshots each glossary term into `site/share-assets/` for social preview cards.
4. **`python scripts/preview-generator.py`** — generates one small share/redirect page per glossary term, injects them into the sitemap, and fixes the FAQ's social-meta tags.
5. **Deploy** — pushes `site/` to GitHub Pages.

Steps 3–4 depend on step 2 having produced `site/`, so order matters.

## Adding content

- **A new gear / territory / crop / dish / tool item:** add an entry to the relevant dict in `data/*.py`. The tooltip renders automatically wherever you use its macro in Markdown (e.g. `{{ gear("Evil Dragon's Blade") }}`).
- **A new page:** create the `.md` file under `docs/`, then add it to the `nav:` tree in `properdocs.yml`.
- **Moving/renaming a page:** add the old path to the `redirects` plugin map in `properdocs.yml` so existing links don't break.

## Deploying

Push to `main`. The workflow builds and deploys automatically. To also post
a Discord announcement, include **`[notify]`** anywhere in the commit
message — the first line becomes the announcement title, the rest the body.

## Config values

The site's URL and path prefix have **one** source: `site_url` in
`properdocs.yml`. `main.py` derives its `prefix` from it, and the scripts
read it via `scripts/site_config.py`. Don't hardcode the domain or
`/BD2-Overview/` anywhere else.
