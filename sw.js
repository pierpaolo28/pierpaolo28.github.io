// Credits to: https://gist.github.com/kosamari/7c5d1e8449b2fbc97d372675f16b566e
var APP_PREFIX = 'PierPaoloIppolitoWebsite_' // Identifier for this app (this needs to be consistent across every cache update)
var VERSION = 'version_01' // Version of the off-line cache (change this value everytime you want to update cache)
var CACHE_NAME = APP_PREFIX + VERSION
var URLS = [ // Add URL you want to cache in this list.
  './', // If you have separate JS/CSS files,
  './index.html', // add path to those files here
  './assets/css/main.css'
]

// Respond with cached resources
self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(request) {
      return request || fetch(e.request)
    })
  )
})

self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      console.log('installing cache : ' + CACHE_NAME)
      return cache.addAll(URLS)
    })
  )
})

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keyList) {
      var cacheWhitelist = keyList.filter(function(key) {
        return key.indexOf(APP_PREFIX)
      })
      cacheWhitelist.push(CACHE_NAME)

      return Promise.all(keyList.map(function(key, i) {
        if (cacheWhitelist.indexOf(key) === -1) {
          console.log('deleting cache : ' + keyList[i])
          return caches.delete(keyList[i])
        }
      }))
    })
  )
})