const CACHE_NAME = "senghor-ia-online-v1";


// Installation du service worker
self.addEventListener("install", event => {

    self.skipWaiting();

});


// Activation
self.addEventListener("activate", event => {

    event.waitUntil(
        caches.keys().then(keys => {

            return Promise.all(
                keys.map(key => caches.delete(key))
            );

        })
    );

});


// Toujours demander au serveur
self.addEventListener("fetch", event => {

    event.respondWith(

        fetch(event.request)
        .catch(() => {

            return new Response(
                `
                <h1>🤖 Senghor IA</h1>
                <h2>❌ Connexion Internet requise</h2>
                <p>Vérifiez votre WiFi ou votre forfait Internet.</p>
                `,
                {
                    headers:{
                        "Content-Type":"text/html"
                    }
                }
            );

        })

    );

});
