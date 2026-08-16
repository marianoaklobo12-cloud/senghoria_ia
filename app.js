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
        Vérifiez votre forfait Internet ou votre WiFi.
        </p>

        <button onclick="location.reload()" 
        style="
        padding:12px 25px;
        border-radius:10px;
        background:#00d9ff;
        ">
        🔄 Réessayer
        </button>

        </div>

        `;

        return false;
    }


    return true;

}



window.addEventListener(
"load",
verifierConnexion
);



window.addEventListener(
"offline",
verifierConnexion
);



// =====================================
// NAVIGATION SENGHOR IA
// =====================================


function ouvrirPage(page){

    if(!verifierConnexion()){

        return;

    }


    window.location.href = page;

}



// =====================================
// BOUTON CREATION VIDEO
// =====================================

let creation =
document.getElementById("creation");


if(creation){

    creation.onclick = function(){

        ouvrirPage(
        "parametres.html"
        );

    };

}



// =====================================
// BOUTONS AUTOMATIQUES
// =====================================


document.querySelectorAll(
"[data-page]"
).forEach(

bouton => {


    bouton.onclick = function(){

        ouvrirPage(
        this.dataset.page
        );

    };


}

