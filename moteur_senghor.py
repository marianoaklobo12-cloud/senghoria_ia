import os
import json
import subprocess

from PIL import Image, ImageDraw

from voix_robot import creer_voix


DOSSIER = "episode_senghor"
VIDEO = "Senghor_episode.mp4"



def charger_demande():

    fichier = "demande_senghor.json"

    if os.path.exists(fichier):

        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)


    return {

        "texte": "Un robot construit une ville futuriste",
        "duree": "1 minute",
        "format": "16:9",
        "voix": "robot amusant",
        "musique": "aventure",
        "langue": "fr"

    }





def creer_dossier():

    os.makedirs(
        DOSSIER,
        exist_ok=True
    )





def creer_scenes(demande):

    texte = demande["texte"]


    scenes = [

        "Introduction",
        "Découverte",
        "Aventure",
        "Construction",
        "Obstacle",
        "Action spectaculaire",
        "Victoire",
        "Conclusion"

    ]


    print("🎬 Création des scènes...")


    for i, titre in enumerate(scenes, 1):

        image = Image.new(
            "RGB",
            (1280,720),
            (5,15,40)
        )


        dessin = ImageDraw.Draw(image)


        contenu = (

            "SENGHOR IA\n\n"
            f"Scène {i}\n"
            f"{titre}\n\n"
            f"{texte}"

        )


        dessin.text(
            (100,150),
            contenu,
            fill=(0,220,255)
        )


        image.save(
            f"{DOSSIER}/scene{i}.png"
        )


    print("✅ Scènes terminées")







def creer_voix_robot(demande):

    print("🎙 Création voix robot...")


    fichier = creer_voix(

        demande["texte"],

        demande.get(
            "voix",
            "robot calme"
        ),

        demande.get(
            "langue",
            "fr"
        )

    )


    print(
        "✅ Voix :",
        fichier
    )


    return fichier







def creer_video(demande):

    print("🎥 Montage vidéo avancé...")


    audio = (
        "audio/"
        + demande.get(
            "voix",
            "robot calme"
        ).replace(" ","_")
        + ".mp3"
    )


    commande = [

        "ffmpeg",
        "-y",

        "-framerate",
        "1",

        "-i",
        f"{DOSSIER}/scene%d.png",

        "-i",
        audio,

        "-filter_complex",

        "[0:v]zoompan=z='min(zoom+0.0015,1.2)':d=125,scale=1280:720[v]",

        "-map",
        "[v]",

        "-map",
        "1:a",

        "-c:v",
        "libx264",

        "-c:a",
        "aac",

        "-shortest",

        "-pix_fmt",
        "yuv420p",

        VIDEO

    ]


    subprocess.run(
        commande
    )


    print(
        "✅ Vidéo finale créée :",
        VIDEO
    )







def lancer():

    print("="*40)

    print("🤖 SENGHOR IA ENGINE")

    print("="*40)


    demande = charger_demande()


    print(
        "Prompt :",
        demande["texte"]
    )


    print(
        "Voix :",
        demande["voix"]
    )


    print(
        "Musique :",
        demande["musique"]
    )


    print(
        "Format :",
        demande["format"]
    )


    creer_dossier()

    creer_scenes(demande)

    creer_voix_robot(demande)

    creer_video(demande)


    print("="*40)

    print("🚀 PRODUCTION TERMINEE")

    print("="*40)





if __name__ == "__main__":

    lancer()
