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

replacement = """<div id="brandName" class="text-[25.1px] sm:text-[22.5px] md:text-[27.5px] font-black text-primary tracking-tighter font-headline uppercase leading-none whitespace-nowrap transition-colors duration-500 flex items-baseline">
        SRI ASHA <span class="text-secondary ml-1.5 sm:ml-2">FORGINGS</span> <span class="text-secondary text-[0.6em] sm:text-[0.45em] md:text-[0.51em] ml-1.5 normal-case font-bold tracking-normal">Pvt Ltd</span>
      </div>
      <div id="brandTag" class="text-[9px] sm:text-[10px] md:text-[12.5px] font-bold text-secondary uppercase leading-none mt-0.5 md:mt-0.5 whitespace-nowrap transition-colors duration-500 tracking-[0.14em] md:tracking-[0.16em]">
        Specialist In Aluminium Alloy Forgings
      </div>"""

for f_name in files_to_update:
    path = os.path.join(r"c:\Desktop\sriasha-main1\sriasha-main", f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Match <div id="brandName"... until the end of the brandTag div
        pattern = re.compile(r'<div\s+id="brandName".*?Specialist In Aluminium Alloy Forgings\s*</div>', re.DOTALL)
        
        new_content = pattern.sub(replacement, content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {f_name}")
    else:
        print(f"File {f_name} not found")
