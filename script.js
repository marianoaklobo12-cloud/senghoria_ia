const bouton = document.querySelector(".creer");
const zone = document.getElementById("description");


let projets = [];



// CRÉER UNE VIDÉO

bouton.addEventListener("click", function(){

let texte = zone.value;


if(texte.trim() === ""){

alert("Décris d'abord ta vidéo.");

return;

}


projets.push(texte);


alert(
"🎬 Senghor IA\n\n" +
"Projet vidéo enregistré :\n\n" +
texte
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





// SAUVEGARDER PROJET

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




// VOIR VIDEOS

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
