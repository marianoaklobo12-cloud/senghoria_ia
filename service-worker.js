const CACHE_NAME = "senghor-ia-v1";

const fichiers = [
  "index.html",
  "style.css",
  "app.js",
  "manifest.json",
  "moteur_ia.js",
  "projets.html",
  "scenario.html",
  "Senghor_episode_final.mp4",
  "images/icon-192.png",
  "images/icon-512.png"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(fichiers))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
