const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
    const page = await browser.newPage();
    
    await page.setViewport({ width: 1200, height: 1080, deviceScaleFactor: 2 });

    const fileUrl = `file://${path.resolve(__dirname, './site/miscellaneous/game-slang/index.html')}`;

    if (!fs.existsSync(path.resolve(__dirname, './site/miscellaneous/game-slang/index.html'))) {
        console.error("Error: Build folder not found! Make sure to run 'mkdocs build' first.");
        process.exit(1);
    }

    await page.goto(fileUrl, { waitUntil: 'networkidle2' });

    const outputDir = path.resolve(__dirname, './site/share-assets');
    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

    const items = await page.$$('.slang-item');
    console.log(`Found ${items.length} slang items. Starting screenshot capture...`);

    for (let item of items) {
        const titleText = await item.$eval('h3', el => el.innerText);
        const slug = titleText.toLowerCase().replace(/ /g, '-').replace(/[^a-z0-9\-]/g, '');

        const boundingBox = await item.boundingBox();

        const imagePath = path.join(outputDir, `${slug}.png`);
        
        if (boundingBox) {
            await page.screenshot({
                path: imagePath,
                clip: {
                    x: boundingBox.x - 20,
                    y: boundingBox.y - 20,
                    width: boundingBox.width + 40,
                    height: boundingBox.height + 40
                }
            });
        } else {
            await item.screenshot({ path: imagePath });
        }

        console.log(` Captured element screenshot for: ${slug}`);
    }

    await browser.close();
    console.log("All screenshots successfully captured!");
})();