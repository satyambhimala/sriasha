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

replacement = """<div class="intro-brand-3d">SRI ASHA <span class="text-[#b5b5b5]">FORGINGS</span> <span class="text-[#b5b5b5] text-[0.6em] normal-case">Pvt Ltd</span>"""

for f_name in files_to_update:
    path = os.path.join(r"c:\Desktop\sriasha-main1\sriasha-main", f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pattern = re.compile(r'<div class="intro-brand-3d.*?Pvt Ltd</span>', re.DOTALL)
        
        new_content = pattern.sub(replacement, content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated loader in {f_name}")
    else:
        print(f"File {f_name} not found")
