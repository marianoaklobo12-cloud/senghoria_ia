import os
import subprocess
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont


DOSSIER = "episode_senghor"
VIDEO = "Senghor_episode.mp4"


def creer_dossier():
    os.makedirs(DOSSIER, exist_ok=True)


def creer_scenes(idee):

    print("🎬 Génération des 8 scènes...")

    scenes = [
        "Introduction",
        "Début de l'aventure",
        "Exploration",
        "Découverte",
        "Grande action",
        "Moment spectaculaire",
        "Victoire",
        "Conclusion"
    ]

    for i, titre in enumerate(scenes, 1):

        image = Image.new(
            "RGB",
            (1280,720),
            (5,15,40)
        )

        dessin = ImageDraw.Draw(image)

        texte = (
            "SENGHOR\n\n"
            f"Scène {i}\n"
            f"{titre}\n\n"
            f"{idee}"
        )

        dessin.text(
            (120,180),
            texte,
            fill=(0,220,255)
        )

        image.save(
            f"{DOSSIER}/scene{i}.png"
        )

    print("✅ 8 scènes terminées")


def creer_voix():

    print("🎙 Création des voix IA...")

    for i in range(1,9):

        texte = (
            f"Bienvenue dans la scène {i} "
            "créée par Senghor."
        )

        audio = gTTS(
            texte,
            lang="fr"
        )

        audio.save(
            f"{DOSSIER}/voix{i}.mp3"
        )

    print("✅ Voix terminées")


def creer_video():

    print("🎥 Création du film...")

    commande = [
        "ffmpeg",
        "-y",
        "-framerate",
        "1",
        "-i",
        f"{DOSSIER}/scene%d.png",
        "-vf",
        "zoompan=z='min(zoom+0.002,1.5)':d=100:s=1280x720",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        VIDEO
    ]

    subprocess.run(commande)

    print("✅ Vidéo créée :", VIDEO)



def lancer():

    print("="*40)
    print("🤖 SENGHOR IA VIDEO ENGINE")
    print("="*40)

    idee = input(
        "Décris ton épisode : "
    )

    creer_dossier()
    creer_scenes(idee)
    creer_voix()
    creer_video()

    print("="*40)
    print("🚀 EPISODE TERMINE")
    print("="*40)



if __name__ == "__main__":
    lancer()
