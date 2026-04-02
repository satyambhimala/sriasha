import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

mobile_nav_replacement = """<!-- Mobile Menu (Hidden on desktop) -->
      <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="gallery.html">Gallery</a>
        <a href="index.html#contact" title="Request a Quote">Request a Quote</a>
      </nav>"""

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Revert Mobile Navigation Menu to minimalist layout
        content = re.sub(
            r'<!-- Mobile Menu \(Hidden on desktop\) -->.*?</nav>',
            mobile_nav_replacement,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Reverted Mobile Navigation to minimalist layout for: {f_name}")
