import subprocess
import os


def effet_robot(entree, sortie):

    commande = [
        "ffmpeg",
        "-y",
        "-i",
        entree,
        "-af",
        "asetrate=16000,aresample=44100,atempo=1.1,flanger",
        sortie
    ]

    subprocess.run(commande)

    print("🤖 Effet robot terminé :", sortie)


entree = "audio/robot_test.mp3"
sortie = "audio/robot_futuriste.mp3"


if os.path.exists(entree):
    effet_robot(entree, sortie)
else:
    print("❌ Le fichier audio/robot_test.mp3 n'existe pas")
