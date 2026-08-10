const bouton = document.querySelector(".creer");
const zone = document.getElementById("description");


let projets = [];



// CRÉATION VIDÉO

bouton.addEventListener("click", function(){

let texte = zone.value;


if(texte.trim() === ""){

alert("Décris d'abord ta vidéo.");

return;

}


projets.push(texte);


alert(
"🎬 Senghor IA\n\nProjet vidéo enregistré :\n\n" 
+ texte
);


});




// ASSISTANT IA

function assistantIA(){

let question =
document.getElementById("questionIA").value;


let reponse =
document.getElementById("reponseIA");


if(question.trim() === ""){

reponse.innerHTML =
"Pose une question.";

return;

}


reponse.innerHTML =
"🤖 Senghor IA :<br><br>" +
"J'ai reçu ta question : " +
question;

}





// PROJETS

function sauverProjet(){


if(projets.length === 0){

document.getElementById("projets").innerHTML =
"Aucun projet enregistré.";

return;

}


document.getElementById("projets").innerHTML =
"✅ Projets :<br>" +
projets.join("<br>");

}





// VIDEOS

function voirVideos(){


if(projets.length === 0){

document.getElementById("listeVideos").innerHTML =
"Aucune vidéo pour le moment.";

return;

}


document.getElementById("listeVideos").innerHTML =
"🎬 Mes créations :<br>" +
projets.join("<br>");

}





// COMPTE

function ouvrirCompte(){

document.getElementById("compte").style.display = "block";

}




function enregistrerCompte(){

let nom =
document.getElementById("nomUtilisateur").value;


let message =
document.getElementById("messageCompte");



if(nom.trim() === ""){

message.innerHTML =
"Écris ton nom.";

return;

}



localStorage.setItem("utilisateur", nom);



message.innerHTML =
"✅ Bienvenue " + nom + " dans Senghor IA";

}
function ouvrirParametres(){

document.getElementById("parametres").style.display = "block";

}



function changerMode(){

document.body.style.background = "#000000";

document.getElementById("infoParametre").innerHTML =
"✅ Mode sombre activé pour Senghor IA";

}
