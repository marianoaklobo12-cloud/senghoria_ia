// =======================================
// SENGHOR IA - CERVEAU SCENARIO AVANCE
// =======================================


function creerScenario(
    texte,
    parametres = {}
){



let duree = parametres.duree || "1 minute";

let format = parametres.format || "16:9";

let voix = parametres.voix || "robot calme";

let musique = parametres.musique || "cinématique";

let langue = parametres.langue || "fr";





let scenario = {


titre:
"Senghor IA - Création vidéo",



idee:
texte,



configuration:{


duree:duree,


format:format,


voix:voix,


musique:musique,


langue:langue


},




style_visuel:{


style:
"Animation 3D futuriste, qualité cinéma, couleurs vives",


camera:
"Mouvements de caméra fluides, plans dynamiques",


ambiance:
"aventure, émotion, imagination"



},




scenes:[



{
numero:1,
titre:"Introduction",
description:
"Présentation de l'univers et du début de l'histoire : "
+ texte
},



{
numero:2,
titre:"Apparition",
description:
"Les personnages principaux apparaissent avec une présentation détaillée."
},



{
numero:3,
titre:"Découverte",
description:
"Le héros découvre un nouvel environnement et commence son aventure."
},



{
numero:4,
titre:"Action",
description:
"Une grande scène d'action avec mouvements de caméra et effets visuels."
},



{
numero:5,
titre:"Obstacle",
description:
"Un problème apparaît et les personnages cherchent une solution."
},



{
numero:6,
titre:"Moment spectaculaire",
description:
"Une scène impressionnante avec émotion et musique."
},



{
numero:7,
titre:"Victoire",
description:
"Le héros réussit sa mission."
},



{
numero:8,
titre:"Conclusion",
description:
"Fin de l'histoire avec une dernière scène mémorable."
}



]

};





// Sauvegarde navigateur

localStorage.setItem(

"scenario_senghor",

JSON.stringify(scenario)

);





return scenario;


}




// Test rapide

function lancerScenario(){


let texte =
localStorage.getItem("DemandeVideo");


if(!texte){

return null;

}



let demande =
JSON.parse(texte);



return creerScenario(

demande.texte,

demande

);



}
