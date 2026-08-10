const bouton = document.querySelector(".creer");
const zone = document.getElementById("description");


bouton.addEventListener("click", function(){

    let texte = zone.value;

    if(texte.trim() === ""){
        alert("Décris d'abord la vidéo que tu veux créer.");
        return;
    }

    alert(
        "🎬 Senghor IA\n\n" +
        "Création de vidéo demandée :\n\n" +
        texte +
        "\n\n⏳ Préparation en cours..."
    );

});


// Assistant IA

function assistantIA(){

    let question = document.getElementById("questionIA").value;
    let reponse = document.getElementById("reponseIA");


    if(question.trim() === ""){
        reponse.innerHTML = "Pose une question.";
        return;
    }


    reponse.innerHTML =
    "🤖 Senghor IA :<br><br>" +
    "J'ai reçu : " + question +
    "<br><br>Je vais préparer une réponse.";
}
