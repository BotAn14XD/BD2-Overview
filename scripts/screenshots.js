// Capture one share-card screenshot per glossary term into site/share-assets/.
//
// Incremental: screenshots are cached in .cache/share-assets/ (which survives
// across builds, unlike site/ which properdocs wipes each time), keyed by a
// hash of each term's rendered HTML. On a build where the slang page didn't
// change, every term is a cache hit and NO new screenshots are taken - the
// cached PNGs are just copied into site/share-assets/. Only terms whose markup
// actually changed are re-shot. This turns a full multi-minute re-shoot of the
// whole glossary into "re-shoot the handful that changed."
//
// Run AFTER `properdocs build`.  Needs Chrome (puppeteer) only to read the DOM
// and shoot the changed items.

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..');
const SLANG_INDEX = path.resolve(ROOT, 'site/misc/slang/index.html');
const SITE_OUT = path.resolve(ROOT, 'site/share-assets');
const CACHE_DIR = path.resolve(ROOT, '.cache/share-assets');
const MANIFEST = path.join(CACHE_DIR, 'manifest.json');

function slugify(title) {
    return title.toLowerCase().replace(/ /g, '-').replace(/[^a-z0-9\-]/g, '');
}

function loadManifest() {
    try {
        return JSON.parse(fs.readFileSync(MANIFEST, 'utf-8'));
    } catch {
        return {};
    }
}

(async () => {
    if (!fs.existsSync(SLANG_INDEX)) {
        console.error("Error: Build folder not found! Make sure to run 'properdocs build' first.");
        process.exit(1);
    }

    fs.mkdirSync(CACHE_DIR, { recursive: true });
    fs.mkdirSync(SITE_OUT, { recursive: true });

    const manifest = loadManifest();
    const nextManifest = {};

    let browser;
    let page;
    let items = [];

    // We only need to launch Chrome if something might need re-shooting. But we
    // must read the DOM to know the hashes, so launch, then decide per item.
    try {
        browser = await puppeteer.launch({ args: ['--no-sandbox'] });
    } catch (err) {
        console.error("\nCould not launch Chrome for screenshots.");
        console.error("If this is your first local build, install the browser once with:");
        console.error("    npx puppeteer browsers install chrome\n");
        console.error("Original error:", err.message);
        process.exit(1);
    }

    try {
        page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 1080, deviceScaleFactor: 2 });
        await page.goto(`file://${SLANG_INDEX}`, { waitUntil: 'networkidle2' });

        items = await page.$$('.slang-item');
        console.log(`Found ${items.length} slang items.`);

        let shot = 0, reused = 0, skipped = 0;

        for (const item of items) {
            const titleText = await item.$eval('h3', el => el.innerText).catch(() => '');
            const slug = slugify(titleText);
            if (!slug) { skipped++; continue; }

            const html = await item.evaluate(el => el.outerHTML);
            const hash = crypto.createHash('sha256').update(html).digest('hex');
            nextManifest[slug] = hash;

            const cachePng = path.join(CACHE_DIR, `${slug}.png`);
            const sitePng = path.join(SITE_OUT, `${slug}.png`);

            // Cache hit: same hash AND the cached image still exists -> reuse it.
            if (manifest[slug] === hash && fs.existsSync(cachePng)) {
                fs.copyFileSync(cachePng, sitePng);
                reused++;
                continue;
            }

            // Miss: (re)shoot into the cache, then copy into the site.
            const box = await item.boundingBox();
            if (box) {
                await page.screenshot({
                    path: cachePng,
                    clip: {
                        x: box.x - 20,
                        y: box.y - 20,
                        width: box.width + 40,
                        height: box.height + 40,
                    },
                });
            } else {
                await item.screenshot({ path: cachePng });
            }
            fs.copyFileSync(cachePng, sitePng);
            shot++;
        }

        // Persist the new manifest and prune cache files no longer referenced.
        fs.writeFileSync(MANIFEST, JSON.stringify(nextManifest, null, 0));
        for (const file of fs.readdirSync(CACHE_DIR)) {
            if (file === 'manifest.json') continue;
            const slug = file.replace(/\.png$/, '');
            if (!(slug in nextManifest)) {
                fs.rmSync(path.join(CACHE_DIR, file), { force: true });
            }
        }

        console.log(`Screenshots: ${shot} shot, ${reused} reused from cache, ${skipped} skipped (no title).`);
        console.log('All screenshots ready in site/share-assets/.');
    } finally {
        await browser.close();
    }
})();
