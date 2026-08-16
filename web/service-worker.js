const CACHE_NAME = "senghor-ia-v2";


const fichiers = [

"./",

"index.html",

"style.css",

"app.js",

"manifest.json",

"assistant.html",

"videos.html",

"projets.html",

"parametres.html",

"compte.html",

"scenario.html",

"moteur_ia.js",

"Senghor_episode_final.mp4",

"images/icon-192.png",

"images/icon-512.png",

"images/scene1.png",

"images/scene2.png",

"images/scene3.png",

"images/scene4.png",

"images/scene5.png",

"images/scene6.png",

"images/scene7.png",

"images/scene8.png"

];



self.addEventListener("install", event => {

event.waitUntil(

caches.open(CACHE_NAME)

.then(cache => {

return cache.addAll(fichiers);

})

);

});




self.addEventListener("activate", event => {

event.waitUntil(

caches.keys().then(keys =>

Promise.all(

keys.map(key => {

if(key !== CACHE_NAME){

return caches.delete(key);

}

})

)

)

);

});




self.addEventListener("fetch", event => {

event.respondWith(

caches.match(event.request)

.then(response => {

return response || fetch(event.request);

})

);

});
