// ===============================
// SENGHOR IA - CONTROLE PRINCIPAL
// ===============================


// Bouton créer vidéo

let boutonCreation = document.querySelector(".create");


if(boutonCreation){

boutonCreation.onclick = function(){

let prompt = document.querySelector("#prompt").value;


if(prompt.trim() === ""){

alert("Décris ta vidéo avant de continuer");

return;

}


// Sauvegarde du prompt

localStorage.setItem(
"prompt_senghor",
prompt
);


// Vérifier les paramètres

let choix = localStorage.getItem(
"choix_video"
);


if(!choix){

alert(
"Faites vos choix dans les paramètres d'abord"
);


window.location.href =
"parametres.html";


return;

}


// Lancer création

lancerVideo();

};

}



// ===============================
// LANCEMENT MOTEUR
// ===============================

function lancerVideo(){


let choix =
JSON.parse(
localStorage.getItem("choix_video")
);


alert(
"🤖 Senghor IA commence la création..."
);


// Envoi au serveur

fetch(
"http://localhost:8080/creer"
)

.then(
response => response.text()
)

.then(
resultat => {


if(resultat === "VIDEO_OK"){

alert(
"✅ Vidéo terminée !"
);


}else{


alert(
"❌ Erreur pendant la création"
);


}


})

.catch(

erreur => {

alert(
"Serveur Senghor IA non actif"
);

}

);


}



// ===============================
// CARTES ACCUEIL
// ===============================


let cartes =
document.querySelectorAll(".card");


if(cartes.length){


cartes[0].onclick=function(){

window.location.href="assistant.html";

};


cartes[1].onclick=function(){

window.location.href="videos.html";

};


cartes[2].onclick=function(){

window.location.href="projets.html";

};


cartes[3].onclick=function(){

window.location.href="parametres.html";

};


}



// ===============================
// MENU BAS
// ===============================


let menu =
document.querySelectorAll("nav button");


if(menu.length){


menu[0].onclick=function(){

window.location.href="index.html";

};


menu[1].onclick=function(){

window.location.href="scenario.html";

};


menu[2].onclick=function(){

window.location.href="videos.html";

};


menu[3].onclick=function(){

window.location.href="compte.html";

};


}
