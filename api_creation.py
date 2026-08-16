import json
import subprocess
import os


FICHIER_CHOIX = "choix_video.json"


def recevoir_choix(
    prompt,
    duree,
    format_video,
    langue,
    voix,
    musique
):

    choix = {

        "prompt": prompt,
        "duree": duree,
        "format": format_video,
        "langue": langue,
        "voix": voix,
        "musique": musique

    }


    with open(
        FICHIER_CHOIX,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            choix,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("✅ Choix enregistrés")
    print(json.dumps(
        choix,
        indent=4,
        ensure_ascii=False
    ))



def lire_choix():

    with open(
        FICHIER_CHOIX,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def lancer_creation():


    if not os.path.exists(FICHIER_CHOIX):

        print("❌ Aucun choix trouvé")

        return



    choix = lire_choix()


    print("🚀 Lancement moteur Senghor IA")
    print(choix)


    subprocess.run(
        [
            "python3",
            "moteur_senghor.py"
        ]
    )




if __name__ == "__main__":


    recevoir_choix(

        "Un robot construit une ville futuriste",

        "1 minute",

        "16:9",

        "fr",

        "robot amusant",

        "aventure"

    )


    lancer_creation()
