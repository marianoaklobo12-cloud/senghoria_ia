// Senghor IA - Gestion complète des boutons

document.addEventListener("DOMContentLoaded", function(){


// Bouton créer vidéo
const boutonCreation = document.querySelector(".create");

boutonCreation.onclick = function(){

let texte = document.querySelector("#prompt").value;

if(texte.trim() === ""){

alert("🤖 Décris d'abord ta vidéo");

return;

}

alert(
"🎬 Senghor IA commence la création...\n\nScénario :\n" + texte
);

// sauvegarde du projet
localStorage.setItem("dernier_projet", texte);

};



// Connexion
const connexion = document.querySelector(".login");

connexion.onclick = function(){

alert(
"👤 Connexion Senghor IA\n\nCompte utilisateur bientôt disponible."
);

};



// Cartes de l'accueil

const cartes = document.querySelectorAll(".card");

cartes[0].onclick = function(){

alert(
"💬 Assistant IA\n\nPose tes questions et crée tes scénarios."
);

};


cartes[1].onclick = function(){

window.location.href="projets.html";

};


cartes[2].onclick = function(){

window.location.href="projets.html";

};


cartes[3].onclick = function(){

alert(
"⚙️ Paramètres\n\nConfiguration Senghor IA."
);

};




// Barre de navigation en bas

const navigation = document.querySelectorAll("nav button");


// Accueil
navigation[0].onclick=function(){

window.location.href="index.html";

};


// Créer
navigation[1].onclick=function(){

document.querySelector("#prompt").focus();

};


// Vidéos
navigation[2].onclick=function(){

window.location.href="projets.html";

};


// Compte
navigation[3].onclick=function(){

alert(
"👤 Compte Senghor IA"
);

};



});
