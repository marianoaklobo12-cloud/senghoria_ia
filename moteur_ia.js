function creerScenario(texte){

let scenario = {

titre: "Senghor IA",

idee: texte,

scenes:[

{
numero:1,
description:"Introduction : "+texte
},

{
numero:2,
description:"Les personnages apparaissent"
},

{
numero:3,
description:"L'aventure commence"
},

{
numero:4,
description:"Action principale"
},

{
numero:5,
description:"Résolution du problème"
},

{
numero:6,
description:"Fin de l'histoire"
}

]

};


localStorage.setItem(
"scenario_senghor",
JSON.stringify(scenario)
);


return scenario;

}
