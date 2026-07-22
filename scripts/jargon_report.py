#!/usr/bin/env python3
"""Report where glossary (slang) terms appear across the content pages.

An authoring aid, NOT part of the build. It answers "which jargon shows up on
this page, in which FORM, and have I linked it yet?" so you can follow the
policy: link the cryptic/abbreviation form (DPS, AoE, ToP), and leave
self-explanatory full proper names (Fiend Hunter) alone.

For every term on a page it breaks the mentions down by surface form, e.g.:

    Area of Effect (game) [abbr] - "AoE" x3 (line 27), full name x1 (line 90)

  * full name  = the term written out in full (the glossary <h3>)
  * "AoE"      = an alias; abbreviation-shaped aliases mark the term [abbr]
  * [abbr] on the term header = a cryptic form appears here -> worth linking

Abbreviations are detected heuristically (short, no spaces, ALL-CAPS or acronym
shaped like AoE / ToP / PvE). It won't be perfect - eyeball it.

Code blocks and inline `code` are masked so they never false-match. Character
and costume proper-noun categories are hidden by default (use --all).

Run from the repo root:
    python scripts/jargon_report.py                 # everything (minus names)
    python scripts/jargon_report.py --unlinked      # only not-yet-linked terms
    python scripts/jargon_report.py --abbr-only     # only terms with a cryptic form here
    python scripts/jargon_report.py --unlinked --abbr-only   # the "what should I link" list
    python scripts/jargon_report.py --all           # include character/costume
    python scripts/jargon_report.py --only game,gear
    python scripts/jargon_report.py --out jargon.txt   # write file directly (UTF-8)

Prefer `--out jargon.txt` over `> jargon.txt`: PowerShell's `>` re-encodes the
output through a legacy codepage and mangles the ── / — characters (you get
"ΓöÇ"). --out writes the file itself as UTF-8-with-BOM, which both VS Code and
Notepad read correctly. Nothing else is modified; it only reads + reports.
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCS = ROOT / "docs"
MIN_TERM_LEN = 3
CATEGORY_CLASSES = {
    "character-tag", "costume-tag", "content-tag", "game-tag",
    "resource-tag", "gear-tag", "miscellaneous-tag",
}
NOISY_DEFAULT = {"character", "costume"}
CONCEPT_CATS = {"game", "gear"}          # concepts: worth linking even in full form


def is_abbrev(s):
    """Short, spaceless, ALL-CAPS or acronym-shaped (AoE, ToP, DPS, PvE, FH)."""
    s = s.strip()
    if not s or " " in s or len(s) > 6:
        return False
    uppers = sum(1 for c in s if c.isupper())
    return s.isupper() or uppers >= 2


class SlangParser(HTMLParser):
    """Pull term / aliases / category from every <li class="slang-item">."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []
        self._cur = None
        self._cap = None
        self._buf = []

    @staticmethod
    def _classes(attrs):
        return (dict(attrs).get("class") or "").split()

    def handle_starttag(self, tag, attrs):
        c = self._classes(attrs)
        if tag == "li" and "slang-item" in c:
            self._cur = {"term": None, "aliases": [], "category": "uncategorized"}
            self._cap = None
            return
        if self._cur is None:
            return
        if tag == "h3" and self._cur["term"] is None:
            self._cap, self._buf = "term", []
        elif tag == "span" and "alias-tag" in c:
            cats = [cls[:-4] for cls in c if cls in CATEGORY_CLASSES]
            if cats:
                self._cur["category"] = cats[0]
            elif set(c) <= {"alias-tag", "rare-tag"}:
                self._cap, self._buf = "alias", []

    def handle_data(self, d):
        if self._cap is not None:
            self._buf.append(d)

    def handle_endtag(self, tag):
        if self._cur is None:
            return
        if tag == "h3" and self._cap == "term":
            self._cur["term"] = "".join(self._buf).strip()
            self._cap = None
        elif tag == "span" and self._cap == "alias":
            self._cur["aliases"].append("".join(self._buf).strip())
            self._cap = None
        elif tag == "li":
            if self._cur["term"]:
                self.items.append(self._cur)
            self._cur = None
            self._cap = None


def slugify(text):
    return re.sub(r"[^a-z0-9\-]", "", text.strip().lower().replace(" ", "-"))


def load_glossary(slang_path):
    """Return:
        forms      - set of surface strings to search for
        form_meta  - form.lower() -> {display, canonical, is_full, is_abbr}
        term_meta  - canonical    -> {slug, cat}
    """
    p = SlangParser()
    p.feed(slang_path.read_text(encoding="utf-8"))
    forms, form_meta, term_meta = set(), {}, {}
    for it in p.items:
        term = it["term"]
        term_meta[term] = {"slug": slugify(term), "cat": it["category"]}
        for i, form in enumerate([term, *it["aliases"]]):
            form = form.strip()
            if len(form) < MIN_TERM_LEN:
                continue
            forms.add(form)
            form_meta.setdefault(form.lower(), {
                "display": form,
                "canonical": term,
                "is_full": (i == 0),
                "is_abbr": is_abbrev(form),
            })
    return forms, form_meta, term_meta


def mask_code(text):
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"```.*?```", blank, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", blank, text)
    return text


def linked_slugs(text):
    return set(re.findall(r"[?&]term=([A-Za-z0-9\-]+)", text))


def build_matcher(forms):
    ordered = sorted(forms, key=len, reverse=True)
    alt = "|".join(re.escape(f) for f in ordered)
    return re.compile(rf"(?<!\w)(?:{alt})(?!\w)", re.IGNORECASE)


def scan_page(path, matcher, form_meta, term_meta):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    masked = mask_code(raw)
    already = linked_slugs(raw)

    # canonical -> {cat, linked, has_abbr, total, forms: {display -> {count, line, is_full, is_abbr}}}
    terms = {}
    for m in matcher.finditer(masked):
        meta = form_meta.get(m.group(0).lower())
        if not meta:
            continue
        canon = meta["canonical"]
        t = terms.get(canon)
        if t is None:
            tm = term_meta[canon]
            t = terms[canon] = {"cat": tm["cat"],
                                "linked": tm["slug"] in already,
                                "has_abbr": False, "total": 0, "forms": {}}
        disp = meta["display"]
        f = t["forms"].get(disp)
        if f is None:
            line = masked.count("\n", 0, m.start()) + 1
            f = t["forms"][disp] = {"count": 0, "line": line,
                                    "is_full": meta["is_full"],
                                    "is_abbr": meta["is_abbr"]}
        f["count"] += 1
        t["total"] += 1
        if meta["is_abbr"]:
            t["has_abbr"] = True
    return terms


def format_forms(forms):
    # most-frequent first; full name breaks ties
    order = sorted(forms.items(), key=lambda kv: (-kv[1]["count"], not kv[1]["is_full"]))
    parts = []
    for disp, f in order:
        label = "full name" if f["is_full"] else f'"{disp}"'
        parts.append(f'{label} x{f["count"]} (line {f["line"]})')
    return ", ".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default=str(DEFAULT_DOCS))
    ap.add_argument("--unlinked", action="store_true", help="only not-yet-linked terms")
    ap.add_argument("--abbr-only", action="store_true",
                    help="only terms that appear in a cryptic/abbreviation form here")
    ap.add_argument("--all", action="store_true", help="include character/costume names")
    ap.add_argument("--only", default="", help="comma list of categories to keep")
    ap.add_argument("-o", "--out",
                    help="write the report to this file as UTF-8 (recommended over > redirect)")
    args = ap.parse_args()

    out_lines = []
    emit = out_lines.append

    docs = Path(args.docs)
    slang = docs / "misc" / "slang.md"
    if not slang.is_file():
        print(f"Could not find glossary at {slang}")
        return 1

    forms, form_meta, term_meta = load_glossary(slang)
    matcher = build_matcher(forms)

    only = {c.strip() for c in args.only.split(",") if c.strip()}
    hidden = set() if (args.all or only) else NOISY_DEFAULT

    emit(f"Loaded {len(term_meta)} glossary terms ({len(forms)} incl. aliases).")
    if hidden:
        emit(f"(hiding categories: {', '.join(sorted(hidden))} - use --all to include)")
    if only:
        emit(f"(showing only categories: {', '.join(sorted(only))})")
    emit("")

    pages = sorted(p for p in docs.rglob("*.md") if p != slang)
    grand = 0

    for page in pages:
        terms = scan_page(page, matcher, form_meta, term_meta)
        terms = {t: r for t, r in terms.items()
                 if r["cat"] not in hidden and (not only or r["cat"] in only)}
        if args.unlinked:
            terms = {t: r for t, r in terms.items() if not r["linked"]}
        if args.abbr_only:
            terms = {t: r for t, r in terms.items() if r["has_abbr"]}
        if not terms:
            continue

        # order: unlinked-with-abbr first, then unlinked concepts, then the rest
        def key(kv):
            _, r = kv
            return (r["linked"], not r["has_abbr"], r["cat"] not in CONCEPT_CATS, -r["total"])

        rel = page.relative_to(docs).as_posix()
        emit(f"── {rel}")
        for term, r in sorted(terms.items(), key=key):
            mark = "linked  " if r["linked"] else "UNLINKED"
            abbr = " [abbr]" if r["has_abbr"] else ""
            if not r["linked"]:
                grand += 1
            emit(f"   [{mark}] {term} ({r['cat']}){abbr} — {format_forms(r['forms'])}")
        emit("")

    emit(f"Total unlinked terms shown: {grand}")
    emit("Policy: link the cryptic form ([abbr]) on its FIRST line; leave plain "
         "full proper names unlinked. Try:  --unlinked --abbr-only")

    report = "\n".join(out_lines) + "\n"
    if args.out:
        # utf-8-sig writes a BOM so Notepad also detects UTF-8. This is written
        # by Python directly, so no shell re-encoding can corrupt it.
        Path(args.out).write_text(report, encoding="utf-8-sig")
        print(f"Wrote {args.out} ({len(out_lines)} lines, UTF-8).")
    else:
        # interactive: force UTF-8 so the console at least doesn't crash
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())