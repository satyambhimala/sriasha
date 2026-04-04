import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

replacement_css = """  .mobile-menu {
    display: none; flex-direction: column; width: 100%;
    position: absolute; top: calc(100% + 4px); left: 0;
    background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(16px);
    border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.18);
    padding: 8px; border: 1px solid rgba(0,0,0,0.05);
  }
  .metallurgy-slide {
    position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
    transition: opacity 1s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0;
  }
  .metallurgy-slide.active { opacity: 1; position: relative; z-index: 1; }
  .mobile-menu.open { display: flex; }
  .mobile-menu a {
    font-family: 'Josefin Sans', sans-serif; font-size: 14px; font-weight: 700; color: #284b63;
    padding: 14px 12px; border-bottom: 1px solid rgba(0,0,0,0.04);
    letter-spacing: 0.04em; text-transform: uppercase; transition: all 0.2s; border-radius: 6px;
  }
  .mobile-menu a:last-child { border-bottom: none; }
  .mobile-menu a:hover { color: #17365d; background-color: rgba(40,75,99,0.06); padding-left: 18px; }"""

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to correctly pop-out the dropdown from the flex row
        content = re.sub(
            r'\.mobile-menu\s*\{.*?\.(?:mobile-menu\s*a:hover|mobile-menu\s*a:\s*hover)\s*\{.*?\}',
            replacement_css,
            content,
            flags=re.DOTALL
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Ejected mobile dropdown logic to absolute position: {f_name}")
