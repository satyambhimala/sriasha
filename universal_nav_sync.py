import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

desktop_nav_replacement = """<!-- Desktop Nav Links -->
      <div class="hidden md:flex items-center space-x-3 lg:space-x-5"> 
        <a href="index.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">Home</a>
        <a href="about.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">About Us</a>
        <a href="gallery.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">Gallery</a>
        <a href="metallurgy.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">Metallurgical Reports</a>
        <a href="Terms.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">Terms &amp; Conditions</a>
        <a href="privacypolicy.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">Privacy Policy</a>
        <a href="Faqs.html" class="text-primary/70 hover:text-secondary transition-all font-headline font-bold tracking-normal uppercase text-[9px] xl:text-[10.5px]">FAQs</a>
        <a href="index.html#contact" class="thermal-gradient-3d text-white px-4 py-2 rounded-md font-headline font-bold uppercase tracking-wide text-[9px] hover:translate-y-[-2px] transition-transform active:scale-95 shadow-lg contact-trigger" title="Request a Quote">Quote</a> 
      </div>"""

mobile_nav_replacement = """<!-- Mobile Menu (Hidden on desktop) -->
      <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="gallery.html">Gallery</a>
        <a href="metallurgy.html">Metallurgical Reports</a>
        <a href="Terms.html">Terms &amp; Conditions</a>
        <a href="privacypolicy.html">Privacy Policy</a>
        <a href="Faqs.html">FAQs</a>
        <a href="index.html#contact" title="Request a Quote">Request a Quote</a>
      </nav>"""

footer_nav_replacement = """<ul class="space-y-2 md:space-y-4 font-body font-light text-slate-300 text-[10.5px] md:text-sm">
            <li><a class="hover:text-white transition-colors" href="index.html">Home</a></li>
            <li><a class="hover:text-white transition-colors" href="about.html">About Us</a></li>
            <li><a class="hover:text-white transition-colors" href="gallery.html">Gallery</a></li>
            <li><a class="hover:text-white transition-colors" href="metallurgy.html">Metallurgical Reports</a></li>
            <li><a class="hover:text-white transition-colors" href="Terms.html">Terms &amp; Conditions</a></li>
            <li><a class="hover:text-white transition-colors" href="privacypolicy.html">Privacy Policy</a></li>
            <li><a class="hover:text-white transition-colors" href="Faqs.html">FAQs</a></li>
          </ul>"""

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update Desktop Nav
        content = re.sub(
            r'<!-- Desktop Nav Links -->.*?</div>',
            desktop_nav_replacement,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Update Mobile Menu
        content = re.sub(
            r'<!-- Mobile Menu \(Hidden on desktop\) -->.*?</nav>',
            mobile_nav_replacement,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Update Footer Pages list
        # Using the heading "Pages" right above it to anchor the replacement reliably
        content = re.sub(
            r'<h4 class="text-white font-headline font-bold uppercase tracking-widest text-xs mb-4 md:mb-6">Pages</h4>\s*<ul.*?</ul>',
            '<h4 class="text-white font-headline font-bold uppercase tracking-widest text-xs mb-4 md:mb-6">Pages</h4>\n          ' + footer_nav_replacement,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Universal Linkings Synced for: {f_name}")
