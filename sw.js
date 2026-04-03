const CACHE_NAME = 'asha-forging-offline-v1';
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
