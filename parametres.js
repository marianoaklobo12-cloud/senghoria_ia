// =================================
// SENGHOR IA - PARAMETRES
// =================================


let choixVideo = JSON.parse(
localStorage.getItem("choix_video")
) || {};


// Tous les boutons de choix

document.querySelectorAll(".choix").forEach(
bouton => {


bouton.onclick = function(){


let type = this.dataset.type;
let valeur = this.dataset.value;


choixVideo[type] = valeur;


// Affichage terminé

this.innerHTML =
"Terminé ✅ " + valeur;


localStorage.setItem(
"choix_video",
JSON.stringify(choixVideo)
);


let message =
document.querySelector("#message");


if(message){

message.innerHTML =
"Choix enregistré : " + type;

}


};


});




// Assemblage vidéo

let assemblage =
document.querySelector("#assembler");


if(assemblage){


assemblage.onclick=function(){


choixVideo.assemblage = true;


localStorage.setItem(
"choix_video",
JSON.stringify(choixVideo)
);


this.innerHTML =
"Assemblage activé ✅";


};

}




// Bouton terminé

let termine =
document.querySelector("#termine");


if(termine){


termine.onclick=function(){


localStorage.setItem(
"choix_video",
JSON.stringify(choixVideo)
);


alert(
"✅ Paramètres terminés"
);


window.location.href =
"index.html";


};


}



// Recherche musique

let recherche =
document.querySelector("#rechercheMusique");


if(recherche){


recherche.onkeyup=function(){


let texte =
this.value.toLowerCase();


document.querySelectorAll(".choix")
.forEach(bouton=>{


if(
bouton.dataset.type==="musique"
){

if(
bouton.dataset.value.includes(texte)
){

bouton.style.display="block";

}else{

bouton.style.display="none";

}


}


});


};

}



console.log(
"Paramètres Senghor IA :",
choixVideo
);
