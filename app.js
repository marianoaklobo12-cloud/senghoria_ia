// Création vidéo

document.querySelector(".create").onclick = function(){

let texte = document.querySelector("#prompt").value;

if(texte === ""){

alert("Décris ta vidéo");

return;

}

alert(
"Senghor IA crée ta vidéo :\n\n" + texte
);

};



// Connexion

document.querySelector(".connexion").onclick=function(){

alert(
"Bienvenue dans Senghor IA\nConnexion bientôt disponible"
);

};



// Cartes de l'écran

let cartes = document.querySelectorAll(".card");


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



// Barre du bas

let menu=document.querySelectorAll("nav button");


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
