// ================================
// CŒUR SENGHOR IA
// Connexion application -> serveur
// ================================


const boutonCreation = document.querySelector(".create");



boutonCreation.onclick = async function(){


let texte = document.querySelector("#prompt").value;



if(texte.trim() === ""){

alert("Décris ta vidéo d'abord");

return;

}




// Récupération des paramètres

let parametres = localStorage.getItem(
"SenghorParametres"
);



if(!parametres){


alert(
"Faites vos choix dans les paramètres d'abord"
);


window.location.href="parametres.html";


return;


}



let choix = JSON.parse(parametres);





let duree = choix.duree || "1 minute";

let format = choix.format || "16:9";

let voix = choix.voix || "robot calme";

let musique = choix.musique || "sans musique";

let langue = choix.langue || "fr";





// Sauvegarde de la demande complète

let demande = {


texte: texte,

duree: duree,

format: format,

voix: voix,

musique: musique,

langue: langue


};



localStorage.setItem(

"DemandeVideo",

JSON.stringify(demande)

);





alert(
"🤖 Senghor IA prépare ta vidéo..."
);





try{


let url =

"http://localhost:8080/creer?" +

new URLSearchParams(demande);





let reponse = await fetch(url);



let resultat = await reponse.text();



alert(resultat);



}

catch(erreur){


alert(
"Erreur connexion au moteur Senghor IA"
);


console.log(erreur);


}



};





// Connexion

const connexion = document.querySelector(".connexion");


if(connexion){


connexion.onclick=function(){


alert(
"Bienvenue dans Senghor IA"
);


};


}






// Navigation cartes


let cartes=document.querySelectorAll(".card");



if(cartes.length>=4){



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






// Barre navigation


let menu=document.querySelectorAll("nav button");



if(menu.length>=4){


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
