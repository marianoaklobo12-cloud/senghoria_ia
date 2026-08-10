const bouton = document.querySelector(".creer");
const zone = document.getElementById("description");


bouton.addEventListener("click", function(){

    let texte = zone.value;

    if(texte.trim() === ""){
        alert("Décris d'abord ta vidéo.");
        return;
    }


    alert(
        "🎬 Senghor IA prépare ta vidéo :\n\n" 
        + texte
    );

});
