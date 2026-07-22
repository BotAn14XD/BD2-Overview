#!/usr/bin/env python3
"""Warn about oversized image assets (advisory only - never fails the build).

Large PNG/JPG illustrations are the easiest way to bloat a page, so this flags
any image under docs/assets/images/ that's bigger than a soft threshold and
isn't a known-large social/banner asset (those live in site-assets/ and are
intentionally heavy for Open Graph cards).

This prints warnings and ALWAYS exits 0 - it's a nudge, not a gate. Run it from
the repo root:  python scripts/check_assets.py
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "docs" / "assets" / "images"

# Soft ceiling for a normal in-page image.
THRESHOLD_KB = 400

# Folders whose large files are intentional (social cards, banners, logo, favicon).
EXEMPT_DIRS = {"site-assets"}

# Formats worth converting to AVIF/WebP when heavy. (AVIF/WebP themselves are
# already efficient, so we don't nag about them.)
HEAVY_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}


def is_exempt(path: Path) -> bool:
    return any(part in EXEMPT_DIRS for part in path.relative_to(IMAGES_DIR).parts)


def main() -> int:
    if not IMAGES_DIR.is_dir():
        print(f"(check_assets) No images dir at {IMAGES_DIR}, nothing to check.")
        return 0

    limit = THRESHOLD_KB * 1024
    offenders = []
    for path in IMAGES_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in HEAVY_EXTS:
            continue
        if is_exempt(path):
            continue
        size = path.stat().st_size
        if size > limit:
            offenders.append((size, path))

    if offenders:
        print(f"WARNING (advisory) - {len(offenders)} image(s) over {THRESHOLD_KB} KB "
              f"outside site-assets/. Consider converting to AVIF/WebP:")
        for size, path in sorted(offenders, reverse=True):
            rel = path.relative_to(ROOT).as_posix()
            print(f"  - {size/1024:8.1f} KB  {rel}")
    else:
        print(f"OK - no oversized images outside site-assets/ (threshold {THRESHOLD_KB} KB).")

    return 0  # advisory: never fail the build


if __name__ == "__main__":
    sys.exit(main())
