import os
import json
import subprocess
from gtts import gTTS
from PIL import Image, ImageDraw


DOSSIER = "episode_senghor"
VIDEO = "Senghor_episode.mp4"


def charger_demande():

    fichier = "demande_senghor.json"

    if os.path.exists(fichier):

        with open(
            fichier,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    return {

        "texte": "Robot dans une ville futuriste",

        "duree": "1 minute",

        "format": "16:9",

        "voix": "robot calme",

        "musique": "aventure",

        "langue": "fr"

    }



def creer_dossier():

    os.makedirs(
        DOSSIER,
        exist_ok=True
    )



def creer_scenes(demande):


    idee = demande["texte"]


    print("🎬 Création des scènes...")


    scenes = [

        "Introduction",

        "Découverte",

        "Aventure",

        "Action",

        "Obstacle",

        "Moment spectaculaire",

        "Victoire",

        "Conclusion"

    ]



    for i,titre in enumerate(scenes,1):


        image = Image.new(

            "RGB",

            (1280,720),

            (5,15,40)

        )


        dessin = ImageDraw.Draw(image)



        texte = (

            "SENGHOR IA\n\n"

            f"Scène {i}\n"

            f"{titre}\n\n"

            f"{idee}"

        )


        dessin.text(

            (100,150),

            texte,

            fill=(0,220,255)

        )



        image.save(

            f"{DOSSIER}/scene{i}.png"

        )



    print("✅ Scènes créées")




def creer_voix(demande):


    print(
        "🎙 Voix robot :",
        demande["voix"]
    )


    texte = demande["texte"]



    voix = gTTS(

        text=texte,

        lang=demande["langue"]

    )


    voix.save(

        f"{DOSSIER}/robot.mp3"

    )



    print("✅ Voix créée")





def creer_video(demande):


    print(

        "🎥 Format :",

        demande["format"]

    )


    commande = [

        "ffmpeg",

        "-y",

        "-framerate",

        "1",

        "-i",

        f"{DOSSIER}/scene%d.png",

        "-c:v",

        "libx264",

        "-pix_fmt",

        "yuv420p",

        VIDEO

    ]



    subprocess.run(
        commande
    )


    print(
        "✅ Vidéo créée :",
        VIDEO
    )






def lancer():


    print("="*40)

    print(
        "🤖 SENGHOR IA ENGINE"
    )

    print("="*40)



    demande = charger_demande()



    print(
        "Prompt :",
        demande["texte"]
    )

    print(
        "Durée :",
        demande["duree"]
    )

    print(
        "Voix :",
        demande["voix"]
    )

    print(
        "Musique :",
        demande["musique"]
    )



    creer_dossier()

    creer_scenes(demande)

    creer_voix(demande)

    creer_video(demande)



    print(
        "🚀 PRODUCTION TERMINÉE"
    )





if __name__ == "__main__":

    lancer()
