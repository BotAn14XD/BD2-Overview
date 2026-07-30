# Full local build - mirrors the GitHub Actions deploy pipeline.
# Run from the repo root:
#     ./build.ps1          full build (needs Chrome for the screenshot step)
#     ./build.ps1 -Quick   skip the Chrome screenshot step (fast "did I break it?" check)
#
# Stops at the first failing step, shows the error, and pauses so the
# window stays open even if you launched it by double-clicking. Exits with a
# non-zero code on failure so it can't be mistaken for success in automation.

param([switch]$Quick)

$ErrorActionPreference = "Stop"
$failed = $false

try {
    Write-Host "==> Validating data files..." -ForegroundColor Cyan
    python scripts/validate_data.py
    if ($LASTEXITCODE -ne 0) { throw "Data validation failed." }

    Write-Host "==> Checking asset sizes (advisory)..." -ForegroundColor Cyan
    python scripts/check_assets.py   # advisory only - we don't check its exit code

    Write-Host "==> Building site..." -ForegroundColor Cyan
    py -m properdocs build
    if ($LASTEXITCODE -ne 0) { throw "properdocs build failed." }

    if ($Quick) {
        Write-Host "==> Quick mode: skipping the Chrome screenshot step." -ForegroundColor Yellow
    }
    else {
        Write-Host "==> Capturing glossary share-card screenshots..." -ForegroundColor Cyan
        node scripts/screenshots.js
        if ($LASTEXITCODE -ne 0) { throw "screenshots.js failed." }
    }

    Write-Host "==> Generating share / redirect pages..." -ForegroundColor Cyan
    python scripts/preview-generator.py
    if ($LASTEXITCODE -ne 0) { throw "preview-generator.py failed." }

    Write-Host "==> Build complete. Output is in .\site" -ForegroundColor Green

    Write-Host "==> Checking for broken links..." -ForegroundColor Cyan
    python scripts/check_links.py
    if ($LASTEXITCODE -ne 0) { throw "Link check failed." }
}
catch {
    Write-Host "`nBUILD FAILED: $_" -ForegroundColor Red
    $failed = $true
}
finally {
    Read-Host "`nPress Enter to close"
}

if ($failed) { exit 1 }
