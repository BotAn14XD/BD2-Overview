#!/usr/bin/env python3
"""Check the built site for broken internal links and missing images.

Scans every .html file under site/, resolves each internal href/src/srcset to
a file on disk, and reports any that don't exist. External links (http, mailto,
tel, ...) and pure "#anchor" links are skipped.

Run this AFTER a full build (build -> screenshots -> preview-generator), so the
generated slang pages exist:
    python scripts/check_links.py
Exits 0 if every internal link and image resolves, 1 (with a list) otherwise.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlsplit, unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_config import SITE_URL, PATH_PREFIX

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"


class RefCollector(HTMLParser):
    """Pull every href / src / srcset URL out of an HTML page."""
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for key in ("href", "src"):
            if d.get(key):
                self.refs.append(d[key])
        if d.get("srcset"):
            for part in d["srcset"].split(","):
                url = part.strip().split(" ")[0]
                if url:
                    self.refs.append(url)


def is_external(url):
    u = (url or "").strip()
    if not u:
        return True
    low = u.lower()
    if low.startswith(("http://", "https://")):
        return not u.startswith(SITE_URL)   # our own domain counts as internal
    return low.startswith(("mailto:", "tel:", "data:", "javascript:", "//"))


def to_local_path(url, html_file):
    """Filesystem path a URL points to, or None if it should be skipped."""
    url, _frag = urldefrag(url)          # drop #anchor
    url = urlsplit(url).path             # drop ?query
    url = unquote(url)
    if not url:
        return None                      # pure #anchor / empty

    if url.startswith(SITE_URL):         # our own absolute URL -> root-absolute
        url = "/" + url[len(SITE_URL):]

    if url.startswith("/"):
        rel = url[len(PATH_PREFIX):] if url.startswith(PATH_PREFIX) else url.lstrip("/")
        return SITE / rel
    return html_file.parent / url        # relative to the current page


def resolves(target):
    if target is None:
        return True
    t = Path(target)
    if t.is_file():
        return True
    if t.is_dir() and (t / "index.html").is_file():
        return True
    return False


def main():
    if not SITE.exists():
        print("site/ not found - run a build first.")
        return 1

    broken = set()
    html_files = list(SITE.rglob("*.html"))
    for hf in html_files:
        parser = RefCollector()
        parser.feed(hf.read_text(encoding="utf-8", errors="ignore"))
        for url in parser.refs:
            if is_external(url):
                continue
            if not resolves(to_local_path(url, hf)):
                broken.add((str(hf.relative_to(SITE)), url))

    if broken:
        print(f"FAIL - {len(broken)} broken internal reference(s):\n")
        for src, url in sorted(broken):
            print(f"  [{src}]  ->  {url}")
        return 1

    print(f"OK - checked {len(html_files)} pages, all internal links and images resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())