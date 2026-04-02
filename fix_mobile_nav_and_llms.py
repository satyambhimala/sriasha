import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"

# 1. Provide an LLM crawler meta-file 
llms_txt_path = os.path.join(base_dir, "llms.txt")
llms_content = """# Sri Asha Forgings

> Precision aluminium alloy open die forging manufacturer in Hyderabad, India.

## Company Overview
Sri Asha Forgings Pvt. Ltd. (est. 2004) is a premier manufacturer of aluminium alloy open die forgings, specializing in high-strength, non-ferrous components for the aerospace, defence, automotive, and heavy engineering sectors.

## Key Products & Capabilities
- **Materials:** Aluminium alloys including AA 2014, 2219, 2618, 5083, 6061, 7075, and Aluminium Lithium Alloy 2195.
- **Products:** Forged rings, discs, blocks, rods, shafts, and customized precision components.
- **Standards:** AMS, MIL, IS, BS, DIN, and ASTM specifications.
- **Services:** Complete manufacturing cycle from billet forging, heat treatment (T6, T652, etc.), to final CNC machining and metallurgical testing (Ultrasonic Testing, hardness).

## Leadership & Contact
- Directors: Manduru Ravi Kumar (MD), Sai Rohit Chowdary (Director)
- Location: Plot No 161A, Phase-II, Cherlapalli, Hyderabad, Telangana 500051, India
- Links: [Official Website](https://www.ashaforging.com/) | [About](https://www.ashaforging.com/about.html) | [Gallery](https://www.ashaforging.com/gallery.html)
"""
with open(llms_txt_path, "w", encoding="utf-8") as f:
    f.write(llms_content)
print("Created llms.txt")

# 2. Fix the Mobile View layout wrapper!
html_files = ["index.html", "Terms.html", "privacypolicy.html", "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"]

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update the parent <nav> flex wrapper to prevent breaking line
        # Replace `flex-wrap` with `flex-nowrap`
        content = content.replace("flex flex-wrap justify-between", "flex flex-nowrap justify-between")
        
        # Ensure the hamburger toggle (3 dots) doesn't squish into oblivion
        # by giving it Tailwind's `shrink-0` class
        content = content.replace('class="md:hidden thermal-gradient-3d', 'class="md:hidden shrink-0 thermal-gradient-3d')
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched mobile flex layout for {f_name}")
