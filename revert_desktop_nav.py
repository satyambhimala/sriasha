import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

desktop_nav_replacement = """<!-- Desktop Nav Links -->
      <div class="hidden md:flex items-center space-x-6 lg:space-x-8">
        <a href="index.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-tight uppercase text-xs">Home</a>
        <a href="about.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-tight uppercase text-xs">About</a>
        <a href="gallery.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-tight uppercase text-xs">Gallery</a>
        <a href="index.html#contact" class="thermal-gradient-3d text-white px-6 py-2 rounded-lg font-headline font-bold uppercase tracking-wider text-[10px] hover:translate-y-[-2px] transition-transform active:scale-95 shadow-lg contact-trigger" title="Request a Quote">Quote</a>
      </div>"""

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update Desktop Nav back to Minimal 4-Link Version
        content = re.sub(
            r'<!-- Desktop Nav Links -->\s*<div class="hidden md:flex.*?</div>',
            desktop_nav_replacement,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Reverted Desktop Navigation to minimalist layout for: {f_name}")
