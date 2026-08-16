function creerVideo(){

let texte=document.getElementById("description").value;


if(texte==""){

document.getElementById("resultat").innerHTML=
"⚠️ Décris d'abord ta vidéo";

return;

}


document.getElementById("resultat").innerHTML=
"🤖 Senghor IA prépare ton scénario...";


setTimeout(()=>{

document.getElementById("resultat").innerHTML=
"✅ Scénario créé ! Génération des images et de la voix...";

},2000);


}



function ouvrirVideos(){

alert(
"🎬 Tes vidéos Senghor IA apparaîtront ici"
);

}



function ouvrirProjets(){

alert(
"📁 Projet sauvegardé dans Senghor IA"
);

}



// Installation PWA

if("serviceWorker" in navigator){

navigator.serviceWorker.register(
"service-worker.js"
);

}
