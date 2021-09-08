let cacheName = "Pier Paolo Ippolito"; // 👈 any unique name
let filesToCache = [ // Add URL you want to cache in this list.
  // '/', // If you have separate JS/CSS files,
  // './index.html', // add path to those files here
  // '/assets/css/main.css',
  // '/assets/img/favicon.jpg',
  // '/assets/img/icons/android-chrome-192x192.png',
  // '/assets/img/icons/android-chrome-256x256.png'
]

self.addEventListener("install", function(event) {
  event.waitUntil(caches.open(cacheName).then((cache) => {
    console.log('installed successfully')
    return cache.addAll(filesToCache);
  }));
});

self.addEventListener('fetch', function(event) {

  if (event.request.url.includes('clean-cache')) {
    caches.delete(cacheName);
    console.log('Cache cleared')
  }

  event.respondWith(caches.match(event.request).then(function(response) {
    if (response) {
      console.log('served form cache')
    } else {
      console.log('Not serving from cache ', event.request.url)
    }
    return response || fetch(event.request);
  }));
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keyList) {
      return Promise.all(keyList.map(function(key) {
        if (key !== cacheName) {
          console.log('service worker: Removing old cache', key);
          return caches.delete(key);
        }
      }));
    })
  );
  return self.clients.claim();
});