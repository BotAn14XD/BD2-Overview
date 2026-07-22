#!/usr/bin/env python3
"""Sanity-check the data files before a build.

Currently checks: every icon path referenced in data/*.py points to a real
file under docs/. Broken image links are the most common failure mode for a
data-driven site, and this catches them before they ship.

Run from the repo root:  python scripts/validate_data.py
Exits 0 if everything is fine, 1 (with a list) if anything is missing.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT))

from data.icons import IMAGES
from data.gear import GEAR_DB
from data.territory import (
    MATERIALS_DB, TERRITORY_DB, CROPS_DB, TOOLS_DB, DISHES_DB,
)

missing = []


def check(path, where):
    """Record `where` if `path` is set but the file doesn't exist under docs/."""
    if not path:
        return
    if not (DOCS / path).is_file():
        missing.append(f"{where}  ->  {path}")


# icons.py:  { key: [path, label] }
for key, info in IMAGES.items():
    check(info[0], f"icons.IMAGES[{key!r}]")

# gear.py:  each entry has an "icon"
for name, item in GEAR_DB.items():
    check(item.get("icon"), f"gear.GEAR_DB[{name!r}]")

# territory materials:  { name: path }
for name, path in MATERIALS_DB.items():
    check(path, f"territory.MATERIALS_DB[{name!r}]")

# the tile DBs:  each entry has an "icon"
for db_name, db in [
    ("TERRITORY_DB", TERRITORY_DB),
    ("CROPS_DB", CROPS_DB),
    ("DISHES_DB", DISHES_DB),
    ("TOOLS_DB", TOOLS_DB),
]:
    for name, item in db.items():
        check(item.get("icon"), f"territory.{db_name}[{name!r}]")

if missing:
    print(f"FAIL - {len(missing)} icon path(s) point to files that don't exist:\n")
    for m in missing:
        print("  -", m)
    sys.exit(1)

print("OK - every icon path in the data files points to a real file.")