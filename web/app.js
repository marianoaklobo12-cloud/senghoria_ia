// Senghor IA - Gestion des boutons

// Bouton créer vidéo
document.querySelector(".create").onclick = function(){

    let texte = document.querySelector("#prompt").value;

    if(texte === ""){
        alert("Décris ta vidéo avant de commencer");
        return;
    }

    localStorage.setItem("scenario", texte);

    alert(
    "🤖 Senghor IA prépare ton scénario :\n\n" 
    + texte
    );

    window.location.href="scenario.html";

};


// Connexion
document.querySelector(".login").onclick=function(){

    alert(
    "🔐 Connexion Senghor IA\n\n" +
    "Création de compte bientôt disponible"
    );

};


// Cartes

let cartes=document.querySelectorAll(".card");


// Assistant IA
cartes[0].onclick=function(){

alert(
"💬 Assistant IA\n\n" +
"Pose tes questions et crée tes histoires."
);

};


// Mes vidéos
cartes[1].onclick=function(){

window.location.href="Senghor_episode_final.mp4";

};


// Mes projets
cartes[2].onclick=function(){

window.location.href="projets.html";

};


// Paramètres
cartes[3].onclick=function(){

alert(
"⚙️ Paramètres\n\n" +
"Langue : Français\n" +
"Version : Senghor IA 1.0"
);

};


// Navigation du bas

let nav=document.querySelectorAll("nav button");


// Accueil
nav[0].onclick=function(){
window.location.href="index.html";
};


// Créer
nav[1].onclick=function(){
document.querySelector("#prompt").focus();
};


// Vidéos
nav[2].onclick=function(){
window.location.href="Senghor_episode_final.mp4";
};


// Compte
nav[3].onclick=function(){

alert(
"👤 Compte Senghor IA\n\n" +
"Connexion bientôt disponible"
);

};


// Chargement scénario existant

let ancien =
localStorage.getItem("scenario");


if(ancien){

document.querySelector("#prompt").value=ancien;

}
