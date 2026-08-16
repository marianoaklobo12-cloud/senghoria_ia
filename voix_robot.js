const voixRobot = {

    joyeux: {
        nom: "Robot joyeux",
        emotion: "heureux et positif"
    },

    amusant: {
        nom: "Robot amusant",
        emotion: "drôle et divertissant"
    },

    geant: {
        nom: "Robot géant",
        emotion: "puissant et impressionnant"
    },

    serieux: {
        nom: "Robot sérieux",
        emotion: "calme et professionnel"
    },

    mysterieux: {
        nom: "Robot mystérieux",
        emotion: "sombre et intrigant"
    },

    energique: {
        nom: "Robot énergique",
        emotion: "rapide et motivant"
    },

    calme: {
        nom: "Robot calme",
        emotion: "doux et reposant"
    }

};


function choisirVoix(type){

    localStorage.setItem(
        "voixRobot",
        JSON.stringify(voixRobot[type])
    );

    return voixRobot[type];

}
