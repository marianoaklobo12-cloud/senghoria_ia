// =====================================
// SENGHOR IA - PARAMETRES VIDEO
// =====================================


// Valeurs par défaut

let choixVideo = {

format: "",
duree: "",
langue: "",
voix: "",
musique: "",
assemblage: false

};



// Charger les anciens choix

let ancien =
localStorage.getItem("choix_video");


if(ancien){

choixVideo = JSON.parse(ancien);

}



// Fonction sauvegarde

function sauvegarder(){

localStorage.setItem(
"choix_video",
JSON.stringify(choixVideo)
);

}



// Fonction bouton terminé

function terminerBouton(bouton){

bouton.innerHTML = "Terminé ✅";

bouton.style.opacity = "0.7";

}



// FORMAT

document.querySelectorAll(".format").forEach(

bouton => {

bouton.onclick = function(){

choixVideo.format =
this.dataset.value ||
this.innerText;


terminerBouton(this);

sauvegarder();

};

});




// DURÉE

document.querySelectorAll(".duree").forEach(

bouton => {

bouton.onclick=function(){


choixVideo.duree =
this.dataset.value ||
this.innerText;


terminerBouton(this);

sauvegarder();


};

});




// LANGUE

document.querySelectorAll(".langue").forEach(

bouton=>{


bouton.onclick=function(){


choixVideo.langue =
this.dataset.value ||
this.innerText;


terminerBouton(this);

sauvegarder();


};


});




// VOIX ROBOT

document.querySelectorAll(".voix").forEach(

bouton=>{


bouton.onclick=function(){


choixVideo.voix =
this.dataset.value ||
this.innerText;


terminerBouton(this);

sauvegarder();


};


});




// MUSIQUE

document.querySelectorAll(".musique").forEach(

bouton=>{


bouton.onclick=function(){


choixVideo.musique =
this.dataset.value ||
this.innerText;


terminerBouton(this);

sauvegarder();


};


});




// ASSEMBLAGE VIDEO

let assemblage =
document.querySelector("#assemblage");


if(assemblage){


assemblage.onclick=function(){


choixVideo.assemblage = true;


this.innerHTML =
"Assemblage activé ✅";


sauvegarder();


};

}



// BOUTON RETOUR

let retour =
document.querySelector("#retour");


if(retour){

retour.onclick=function(){

window.location.href="index.html";

};

}



// Vérification

console.log(
"Senghor IA paramètres :",
choixVideo
);
