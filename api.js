
async function demanderIA(question) {

    let reponse =
    document.getElementById("reponseIA");


    reponse.innerHTML =
    "🤖 Senghor IA réfléchit...";


    try {

        let resultat = await fetch(
            "https://TON_SERVEUR.com/assistant",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        let donnees = await resultat.json();


        reponse.innerHTML =
        "🤖 Senghor IA :<br><br>" +
        donnees.reponse;


    } catch(error) {


        reponse.innerHTML =
        "Erreur de connexion au serveur IA.";

    }

}
