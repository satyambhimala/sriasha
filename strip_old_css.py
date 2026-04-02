import os
import re

files_to_update = [
    "Terms.html",
    "privacypolicy.html",
    "metallurgy.html",
    "Faqs.html",
    "about.html",
    "gallery.html",
    "404.html"
]

for f_name in files_to_update:
    path = os.path.join(r"c:\Desktop\sriasha-main1\sriasha-main", f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pattern = re.compile(r'/\*\s*──\s*NAV REFINEMENT.*?(?:overflow:\s*hidden\s*;|overflow:\s*hidden;\s*\}|overflow:\s*hidden\s*\}\s*)[\n\r]*\s*\}?', re.DOTALL | re.IGNORECASE)
        # Wait, some places might just not match easily.
        # Let's just remove the specific block:
        
        # A simpler way is to find the comment and the next 5 rules.
        pattern2 = re.compile(r'[ \t]*/\*\s*──\s*NAV REFINEMENT[^\n]*\n.*?#brandTag[^}]+\}', re.DOTALL)
        
        new_content = pattern2.sub('', content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Cleaned {f_name}")
    else:
        print(f"File {f_name} not found")
