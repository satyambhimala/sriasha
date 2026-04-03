import os
import re

files_to_update = [
    "index.html",
    "Terms.html",
    "privacypolicy.html",
    "metallurgy.html",
    "Faqs.html",
    "about.html",
    "gallery.html",
    "404.html"
]

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"

for f_name in files_to_update:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Remove fitTagline script logic completely to prevent UI locking and lag.
        # It's usually block starting with /* ══ TAGLINE FIT (mobile only) ══ */ up to fitTagline();
        # This will fix any lags and stucks caused by conflicting !important CSS and JS while loops
        pattern_fit = re.compile(r'/\*\s*[=═]+\s*TAGLINE FIT \(mobile only\)\s*[=═]+\s*\*/.*?fitTagline\(\);', re.DOTALL)
        content = pattern_fit.sub('', content)
        
        # also removing any other variants (e.g., using == TAGLINE FIT)
        pattern_fit2 = re.compile(r'/\*\s*==\s*TAGLINE FIT \(mobile only\)\s*==\s*\*/.*?fitTagline\(\);', re.DOTALL)
        content = pattern_fit2.sub('', content)

        # 2. Change "Get Quote" or "Get a Quote" to "Request a Quote" in navbar strings to push Sitelink explicitly
        content = re.compile(r'>Get Quote<', re.IGNORECASE).sub('>Request a Quote<', content)
        content = re.compile(r'>Get a Quote<', re.IGNORECASE).sub('>Request a Quote<', content)
        # Add title tags to help SEO sitelinks
        content = re.sub(r'(<a\s+href="index\.html#contact"[^>]*?)>', r'\1 title="Request a Quote">', content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched {f_name}")
    else:
        print(f"File {f_name} not found")

