import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # This regex matches the orphaned chunk of the fitTagline loop that was left over 
        # in Faqs.html and causing a syntax error (preventing the page from loading)
        pattern = re.compile(r'\s*var target = bn\.offsetWidth;.*?\}\s*</script>', re.DOTALL)
        
        # We replace it with just the closing script tag
        new_content = pattern.sub('\n</script>', content)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed broken script syntax in {f_name}")
