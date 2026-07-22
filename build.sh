#!/usr/bin/env bash
# Full local build - mirrors the GitHub Actions deploy pipeline.
# Run from the repo root:  ./build.sh
# `set -e` stops at the first failing step, so you catch breakage before pushing.
set -euo pipefail

echo "==> Validating data files..."
python scripts/validate_data.py

echo "==> Checking asset sizes (advisory)..."
python scripts/check_assets.py || true   # advisory only - never blocks the build

echo "==> Building site..."
properdocs build

echo "==> Capturing glossary share-card screenshots..."
node scripts/screenshots.js

echo "==> Generating share / redirect pages..."
python scripts/preview-generator.py

echo "==> Checking for broken links..."
python scripts/check_links.py

echo "==> Build complete. Output is in ./site"
