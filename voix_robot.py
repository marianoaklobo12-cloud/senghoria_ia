from gtts import gTTS
import os


def creer_voix():

    if not os.path.exists("audio"):
        os.makedirs("audio")

    if os.path.exists("texte_scene.txt"):

        with open("texte_scene.txt", "r", encoding="utf-8") as f:
            texte = f.read()

    else:
        texte = "Bonjour, je suis le robot de Senghor IA"


    fichier = "audio/robot_futuriste.mp3"


    voix = gTTS(
        text=texte,
        lang="fr",
        slow=False
    )


    voix.save(fichier)


    print("🤖 Voix créée :", fichier)



creer_voix()
