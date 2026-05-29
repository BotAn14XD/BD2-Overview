import os
import re
import html
import shutil

html_path = "site/misc/slang/index.html"
output_base = "site/misc/slang"

if os.path.exists(output_base):
    print(f"Clearing old generated subfolders from '{output_base}'...")
    for item in os.listdir(output_base):
        item_path = os.path.join(output_base, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
else:
    os.makedirs(output_base, exist_ok=True)

if not os.path.exists(html_path):
    print(f"Error: Could not find build file at {html_path}")
    exit(1)

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

slang_blocks = re.findall(r'<li\s+class="slang-item"[^>]*>(.*?)</li>', html_content, re.DOTALL)

generated_count = 0

for block in slang_blocks:
    title_match = re.search(r'<h3>(.*?)</h3>', block, re.DOTALL)
    if not title_match:
        continue
    raw_term = title_match.group(1).strip()
    
    desc_match = re.search(r'<p>(.*?)</p>', block, re.DOTALL)
    if not desc_match:
        continue
    definition = desc_match.group(1).strip()
    
    definition = re.sub(r'<[^>]+>', '', definition)
    definition = html.unescape(definition)

    term_slug = raw_term.lower().replace(" ", "-")
    term_slug = re.sub(r'[^a-z0-9\-]', '', term_slug)

    if len(definition) > 160:
        definition = definition[:157] + "..."

    img_path = f"share-assets/{term_slug}.png"
    
    term_dir = os.path.join(output_base, term_slug)
    os.makedirs(term_dir, exist_ok=True)
    
    payload = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{raw_term} - Tactical Compendium</title>
    <meta property="og:title" content="{raw_term} - Brown Dust II Glossary Definition">
    <meta property="og:description" content="{definition}">
    <meta property="og:image" content="https://botan14xd.github.io/BD2-Overview/{img_path}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta http-equiv="refresh" content="0; url=/BD2-Overview/misc/slang?term={term_slug}">
    </head>
    <body>
    <p>Redirecting to Tactical Compendium... If not automated, <a href="/BD2-Overview/misc/slang?term={term_slug}">click here</a>.</p>
</body>
</html>"""

    with open(os.path.join(term_dir, "index.html"), "w", encoding="utf-8") as out_f:
        out_f.write(payload)

    alias_tags = re.findall(r'<span\s+class="alias-tag"[^>]*>(.*?)</span>', block, re.DOTALL)
    for alias in alias_tags:
        cleaned_alias = alias.strip().lower()
        if "ignore-exact" in cleaned_alias or "content" in cleaned_alias:
            continue
            
        alias_slug = cleaned_alias.replace(" ", "-")
        alias_slug = re.sub(r'[^a-z0-9\-]', '', alias_slug)
        
        if alias_slug and alias_slug != term_slug:
            alias_dir = os.path.join(output_base, alias_slug)
            
            if os.path.exists(alias_dir):
                combined_slug = f"{alias_slug}-{term_slug}"
                alias_dir = os.path.join(output_base, combined_slug)
                print(f"Conflict found for alias '{alias_slug}'. Created specific route: /share/{combined_slug}")
            
            os.makedirs(alias_dir, exist_ok=True)
            
            with open(os.path.join(alias_dir, "index.html"), "w", encoding="utf-8") as alias_f:
                alias_f.write(payload)
        
    generated_count += 1

print(f"Success! Automatically processed {generated_count} landing page proxy routes with screenshot assets.")
