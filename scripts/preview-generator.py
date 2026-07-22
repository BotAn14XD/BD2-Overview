#!/usr/bin/env python3
"""Generate one small share/redirect page per glossary term.

Runs AFTER `properdocs build`, on the built `site/misc/slang/index.html`. For
every glossary entry it writes a tiny `misc/slang/<slug>/index.html` whose only
job is to carry per-term Open Graph / Twitter meta (so a link to a specific
term unfurls with that term's share-card screenshot) and then meta-refresh the
visitor to the real anchored page.

These per-term pages are REDIRECTS, so they exist purely for social-share
unfurls - they are NOT added to the sitemap and are marked `noindex`, because a
sitemap should only list real 200-OK pages (redirect URLs waste crawl budget
and send mixed indexing signals). The actual glossary content lives, and gets
indexed, on the single `misc/slang/` page.

Parsing note: the slang markup is read with a real HTML parser
(`html.parser.HTMLParser`), not regex, so a change to the template (attribute
order, an extra wrapper, entities in a definition) doesn't silently break the
extraction. The parser mirrors the old regex's semantics exactly:
  * an item is a  <li class="slang-item">
  * its term is the first  <h3>
  * its definition is the first  <p>
  * an alias is a  <span>  whose class is exactly  "alias-tag"  or
    "alias-tag rare-tag"  (category chips like  "alias-tag resource-tag
    ignore-exact"  are NOT aliases and are skipped, same as before).

The FAQ social-meta fix that used to live here has been removed: it's now done
declaratively in the page front matter + overrides/main.html (see FAQ.md's
`image` / `card_type` keys), so there's no post-build HTML surgery anymore.
"""
import os
import re
import html
import shutil
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_config import SITE_URL, PATH_PREFIX

HTML_PATH = "site/misc/slang/index.html"
OUTPUT_BASE = "site/misc/slang"

MAX_DESC = 160  # OG description truncation length


class SlangParser(HTMLParser):
    """Collect {term, definition, aliases} for every <li class="slang-item">."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []
        self._cur = None          # the item dict currently being built
        self._capture = None      # "term" | "def" | "alias" while inside that tag
        self._buf = []            # text nodes accumulated for the active capture
        self._got_def = False     # only the FIRST <p> is the definition

    @staticmethod
    def _classes(attrs):
        d = dict(attrs)
        return (d.get("class") or "").split()

    def handle_starttag(self, tag, attrs):
        classes = self._classes(attrs)

        if tag == "li" and "slang-item" in classes:
            # Start a fresh item (ignore any stray nesting: last one wins, as before)
            self._cur = {"term": None, "definition": None, "aliases": []}
            self._got_def = False
            self._capture = None
            return

        if self._cur is None:
            return

        if tag == "h3" and self._cur["term"] is None:
            self._capture, self._buf = "term", []
        elif tag == "p" and not self._got_def:
            self._capture, self._buf = "def", []
        elif tag == "span" and "alias-tag" in classes and set(classes) <= {"alias-tag", "rare-tag"}:
            # exactly "alias-tag" or "alias-tag rare-tag" -> a real alias chip
            self._capture, self._buf = "alias", []

    def handle_data(self, data):
        if self._capture is not None:
            self._buf.append(data)

    def handle_endtag(self, tag):
        if self._cur is None:
            return

        if tag == "h3" and self._capture == "term":
            self._cur["term"] = "".join(self._buf).strip()
            self._capture = None
        elif tag == "p" and self._capture == "def":
            self._cur["definition"] = "".join(self._buf).strip()
            self._got_def = True
            self._capture = None
        elif tag == "span" and self._capture == "alias":
            self._cur["aliases"].append("".join(self._buf).strip())
            self._capture = None
        elif tag == "li" and self._cur is not None:
            if self._cur["term"]:            # skip empty template rows
                self.items.append(self._cur)
            self._cur = None
            self._capture = None


def slugify(text):
    slug = text.strip().lower().replace(" ", "-")
    return re.sub(r"[^a-z0-9\-]", "", slug)


def make_payload(term, definition):
    """The tiny redirect/share page for one term. Attribute values are escaped
    so a quote or angle bracket in a term/definition can't break the meta tags.
    Marked noindex: it's a share-card redirect, not an indexable page."""
    e_term = html.escape(term, quote=True)
    e_def = html.escape(definition, quote=True)
    slug = slugify(term)
    img_path = f"share-assets/{slug}.png"
    dest = f"{PATH_PREFIX}misc/slang?term={slug}"
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex,follow">
    <title>{e_term} - Tactical Compendium</title>
    <meta property="og:title" content="{e_term} - Brown Dust II Glossary Definition">
    <meta property="og:description" content="{e_def}">
    <meta property="og:image" content="{SITE_URL}{img_path}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta http-equiv="refresh" content="0; url={dest}">
    </head>
    <body>
    <p>Redirecting to Tactical Compendium... If not automated, <a href="{dest}">click here</a>.</p>
</body>
</html>"""


def write_route(slug, payload):
    route_dir = os.path.join(OUTPUT_BASE, slug)
    os.makedirs(route_dir, exist_ok=True)
    with open(os.path.join(route_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(payload)


def generate_routes():
    if not os.path.exists(HTML_PATH):
        print(f"Error: Could not find build file at {HTML_PATH}")
        sys.exit(1)

    # clear previously generated per-term subfolders (keep files like index.html)
    if os.path.exists(OUTPUT_BASE):
        print(f"Clearing old generated subfolders from '{OUTPUT_BASE}'...")
        for item in os.listdir(OUTPUT_BASE):
            item_path = os.path.join(OUTPUT_BASE, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
    else:
        os.makedirs(OUTPUT_BASE, exist_ok=True)

    parser = SlangParser()
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        parser.feed(f.read())

    count = 0
    for item in parser.items:
        term = item["term"]
        definition = item["definition"] or ""
        if len(definition) > MAX_DESC:
            definition = definition[: MAX_DESC - 3] + "..."

        term_slug = slugify(term)
        if not term_slug:
            continue

        payload = make_payload(term, definition)
        write_route(term_slug, payload)

        for alias in item["aliases"]:
            cleaned = alias.strip().lower()
            if not cleaned or "ignore-exact" in cleaned or "content" in cleaned:
                continue
            alias_slug = slugify(cleaned)
            if not alias_slug or alias_slug == term_slug:
                continue

            target = alias_slug
            if os.path.exists(os.path.join(OUTPUT_BASE, alias_slug)):
                target = f"{alias_slug}-{term_slug}"
                print(f"Conflict for alias '{alias_slug}'. Created specific route: /share/{target}")
            write_route(target, payload)

        count += 1

    print(f"Success! Processed {count} share-card redirect routes (not indexed, not in sitemap).")
    return count


def main():
    generate_routes()


if __name__ == "__main__":
    main()