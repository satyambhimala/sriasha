import os
import json
import re

# Target directory
base_dir = r"c:\Desktop\sriasha\sriasha-main"

# HTML files to check
html_files = [
    "index.html", "about.html", "gallery.html", "metallurgy.html", 
    "Faqs.html", "Terms.html", "privacypolicy.html", "404.html"
]

def validate_seo(file_path):
    print(f"\n--- Checking {os.path.basename(file_path)} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # 1. Check for valid JSON-LD
    script_pattern = re.compile(r'<script\s+type="application/ld\+json">(.*?)</script>', re.DOTALL)
    scripts = script_pattern.findall(content)
    
    if not scripts:
        errors.append("No JSON-LD script found.")
    else:
        for idx, script_text in enumerate(scripts):
            try:
                data = json.loads(script_text.strip())
                print(f"  [v] JSON-LD {idx+1} is valid.")
            except Exception as e:
                errors.append(f"Invalid JSON in block {idx+1}: {e}")
                
        if len(scripts) > 1:
            print(f"  [!] Found {len(scripts)} separate JSON-LD blocks. Consolidating is usually better.")

    # 2. Check for duplicate meta director/managing-director tags
    director_metas = re.findall(r'<meta name="director" content="([^"]+)">', content)
    md_metas = re.findall(r'<meta name="managing-director" content="([^"]+)">', content)
    
    if len(director_metas) != len(set(director_metas)):
        errors.append("Duplicate director meta tags found.")
    
    # 3. Check for open die forging in meta description (consistency check)
    if "aluminium forging" not in content.lower() and "index.html" in file_path:
        errors.append("Primary keyword 'aluminium forging' not found in content.")

    # 4. Check for broken or relative og:image/twitter:image
    og_image = re.search(r'<meta property="og:image" content="([^"]+)">', content)
    if og_image:
        img_url = og_image.group(1)
        if not img_url.startswith("http"):
            errors.append(f"og:image uses a relative path: {img_url}")
            
    # 5. Check for trailing backslashes/quotes that regex might have left
    # Search for things like ">"> or similar anomalies
    if '">">' in content:
        errors.append("Potential syntax leak (extra >) found.")

    if errors:
        for err in errors:
            print(f"  [ERR] {err}")
    else:
        print("  [OK] No major SEO structure errors found.")
    return errors

all_errors = {}
for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        errs = validate_seo(path)
        if errs:
            all_errors[f_name] = errs
    else:
        print(f"Skipping {f_name} (not found)")

if not all_errors:
    print("\n[SUCCESS] All pages passed SEO validation.")
else:
    print(f"\n[FAIL] Found errors in {len(all_errors)} files.")
