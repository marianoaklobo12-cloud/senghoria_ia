
const bouton = document.querySelector(".creer");
const zone = document.getElementById("description");


bouton.addEventListener("click", function(){

    let texte = zone.value;

    if(texte.trim() === ""){
        alert("Décris d'abord ta vidéo.");
        return;
    }

    alert("🎬 Senghor IA prépare ta vidéo :\n\n" + texte);

});


function assistantIA(){

    let question = document.getElementById("questionIA").value;
    let reponse = document.getElementById("reponseIA");


    if(question.trim() === ""){
        reponse.innerHTML = "Pose une question.";
        return;
    }


    reponse.innerHTML =
    "🤖 Senghor IA :\n\n" +
    "J'ai reçu ta question : " + question +
    "<br><br>Je prépare une réponse intelligente...";
}
