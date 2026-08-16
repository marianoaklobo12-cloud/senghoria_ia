// =====================================
// SENGHOR IA - CONTROLE CONNEXION
// =====================================

function verifierConnexion() {

    if (!navigator.onLine) {

        document.body.innerHTML = `

        <div style="
        background:#08152b;
        color:white;
        height:100vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        text-align:center;
        font-family:Arial;
        padding:20px;
        ">

        <h1>🤖 Senghor IA</h1>

        <h2>❌ Connexion Internet requise</h2>

        <p>
        Aucun accès Internet détecté.
        </p>

        <p>
        Vérifiez votre forfait Internet ou votre connexion WiFi.
        </p>

        <button onclick="location.reload()" style="
        padding:12px 25px;
        border:none;
        border-radius:10px;
        background:#00d9ff;
        color:#08152b;
        font-size:16px;
        ">
        🔄 Réessayer
        </button>

        </div>

        `;

        return false;

    }

    return true;

}


// Vérification au démarrage
window.addEventListener(
    "load",
    verifierConnexion
);


// Vérification si Internet coupe pendant l'utilisation
window.addEventListener(
    "offline",
    verifierConnexion
);



// =====================================
// BOUTON CREATION VIDEO
// =====================================

const boutonCreation = document.getElementById("creation");


if (boutonCreation) {

    boutonCreation.addEventListener(
        "click",
        () => {

            if (!verifierConnexion()) {

                return;

            }


            window.location.href =
            "parametres.html";

        }
    );

}
