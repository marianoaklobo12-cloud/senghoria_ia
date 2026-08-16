from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)


@app.route("/voix", methods=["POST"])
def creer_voix():

    data = request.json

    texte = data["texte"]
    nom = data["nom"]

    dossier = "audio"

    if not os.path.exists(dossier):
        os.makedirs(dossier)

    fichier = f"{dossier}/{nom}.mp3"

    voix = gTTS(
        text=texte,
        lang="fr"
    )

    voix.save(fichier)

    return jsonify({
        "message":"Voix créée",
        "fichier":fichier
    })


app.run(
    host="0.0.0.0",
    port=5000
)
