async function demanderIA(question) {

    let reponse =
    document.getElementById("reponseIA");


    reponse.innerHTML =
    "🤖 Senghor IA réfléchit...";


    // Connexion future avec le serveur IA

    setTimeout(() => {

        reponse.innerHTML =
        "🤖 Senghor IA :\n\n" +
        "Je prépare une réponse intelligente à : "
        + question;

    }, 1500);

}
