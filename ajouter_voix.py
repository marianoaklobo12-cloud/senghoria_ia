import subprocess
import os


video = "Senghor_episode.mp4"
audio = "audio/robot_futuriste.mp3"
sortie = "Senghor_episode_avec_voix.mp4"


if not os.path.exists(video):
    print("❌ Vidéo introuvable")
    exit()

if not os.path.exists(audio):
    print("❌ Voix introuvable")
    exit()


print("🎙️ Ajout de la voix Robot...")


commande = [
    "ffmpeg",
    "-y",
    "-i",
    video,
    "-i",
    audio,
    "-c:v",
    "copy",
    "-c:a",
    "aac",
    "-shortest",
    sortie
]


subprocess.run(commande)


print("✅ Vidéo finale créée :", sortie)
