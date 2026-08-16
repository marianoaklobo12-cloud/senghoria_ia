function creerVideo(){

    let resultat = document.getElementById("resultat");

    let duree = document.getElementById("duree").value;


    resultat.innerHTML =
    "⏳ Senghor IA démarre...\nDurée scène : "
    + duree + " secondes";


    fetch(
    "http://127.0.0.1:8080/creer?duree=" + duree
    )

    .then(response => response.text())


    .then(data => {


        if(data === "VIDEO_OK"){


            resultat.innerHTML =
            "✅ Vidéo terminée !<br>" +
            "Durée : " + duree +
            " secondes";


        }

        else{


            resultat.innerHTML =
            "❌ Erreur moteur : " + data;


        }


    })


    .catch(error => {


        resultat.innerHTML =
        "❌ Serveur Senghor IA non connecté";


    });


}
