import os

sw_content = """const CACHE_NAME = 'asha-forging-offline-v1';
const OFFLINE_URL = '/404.html';

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Setting {cache: 'reload'} guarantees we fetch the latest 404.html to cache
    await cache.add(new Request(OFFLINE_URL, { cache: 'reload' }));
  })());
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    if ('navigationPreload' in self.registration) {
      await self.registration.navigationPreload.enable();
    }
  })());
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Only override navigation requests (when a user visits a browser page)
  if (event.request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const preloadResponse = await event.preloadResponse;
        if (preloadResponse) { return preloadResponse; }
        
        // Always try to fetch from the network first
        const networkResponse = await fetch(event.request);
        return networkResponse;
      } catch (error) {
        // If the network fails (user is offline), serve the local 404 page!
        const cache = await caches.open(CACHE_NAME);
        const cachedResponse = await cache.match(OFFLINE_URL);
        return cachedResponse;
      }
    })());
  }
});
"""

sw_path = r"c:\Desktop\sriasha-main1\sriasha-main\sw.js"
with open(sw_path, "w", encoding="utf-8") as f:
    f.write(sw_content)
print("Created sw.js")

# Modify all HTML files to register the service worker
files_to_update = [
    "index.html",
    "Terms.html",
    "privacypolicy.html",
    "metallurgy.html",
    "Faqs.html",
    "about.html",
    "gallery.html",
    "404.html"
]

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"
script_injection = """
  <!-- Offline Service Worker -->
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').catch(function(err) {
          console.log('Service Worker registration failed: ', err);
        });
      });
    }
  </script>
</body>"""

for f_name in files_to_update:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<!-- Offline Service Worker -->" not in content and "serviceWorker" not in content:
            content = content.replace("</body>", script_injection)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected script into {f_name}")
    else:
        print(f"File {f_name} not found")

# Let's also append the wildcard 404 fallback to _redirects for Cloudflare explicitly
redirects_path = os.path.join(base_dir, "_redirects")
if os.path.exists(redirects_path):
    with open(redirects_path, "a", encoding="utf-8") as f:
        f.write("\n/*  /404.html  404\n")
    print("Added wildcard 404.html fallback to _redirects")
