import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

interceptor_script = """
    <!-- Page Transition Interceptor -->
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('a').forEach(link => {
          if (link.hostname === window.location.hostname && link.getAttribute('href') && !link.getAttribute('href').startsWith('tel:') && !link.getAttribute('href').startsWith('mailto:')) {
            // Only trigger if going to a different page route
            if (link.pathname !== window.location.pathname) {
              link.addEventListener('click', function(e) {
                // Allow new tab clicks to work normally
                if (e.ctrlKey || e.metaKey || this.target === '_blank') return;
                
                e.preventDefault();
                const href = this.href;
                const overlay = document.getElementById('intro-overlay');
                
                if (overlay) {
                  // Re-enable and show the 3D loader
                  overlay.classList.remove('phase-exit');
                  overlay.style.display = 'flex';
                  overlay.style.visibility = 'visible';
                  overlay.style.opacity = '1';
                  
                  // Restart the loader animation bar
                  const barFill = document.getElementById('introBarFill');
                  if (barFill) {
                    barFill.style.transition = 'none';
                    barFill.style.width = '0%';
                    setTimeout(() => {
                      barFill.style.transition = 'width 1s cubic-bezier(0.65, 0, 0.35, 1)';
                      barFill.style.width = '60%';
                    }, 10);
                  }
                  
                  // Navigate in background while loader processes
                  setTimeout(() => {
                    window.location.href = href;
                  }, 150);
                } else {
                  window.location.href = href;
                }
              });
            }
          }
        });
      });
    </script>
"""

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Inject the page interceptor script right before the closing </body> tag
        if "Page Transition Interceptor" not in content:
            content = content.replace("</body>", interceptor_script + "\n</body>")
        
        # 2. Fix the Hero Banner Crossfade Flicker in index.html!
        # The crossfade glitch happens because the container is white, so when two images 
        # fade into each other at 50% opacity, the white background flashes through.
        # Adding a dark background to the housing wrapper eliminates the bright strobe flicker forever.
        if f_name == "index.html":
            content = content.replace('class="w-full h-full rounded-[24px] overflow-hidden relative"', 
                                      'class="w-full h-full rounded-[24px] overflow-hidden relative bg-[#0a1118]"')
            content = content.replace('class="w-full h-full rounded-[28px] overflow-hidden relative"', 
                                      'class="w-full h-full rounded-[28px] overflow-hidden relative bg-[#0a1118]"')

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Upgraded {f_name} with Loader Interceptor & Anti-Flicker Patch")
