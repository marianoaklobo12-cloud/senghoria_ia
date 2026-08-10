const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());


// Route de test IA

app.post("/assistant", (req, res) => {

    const question = req.body.question;


    if (!question) {

        return res.json({
            reponse: "Pose une question."
        });

    }


    res.json({

        reponse:
        "🤖 Senghor IA a reçu ta question : " 
        + question +
        "\n\nConnexion IA réelle à ajouter."

    });

});



app.listen(3000, () => {

    console.log(
        "Serveur Senghor IA démarré"
    );

});
