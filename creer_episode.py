import subprocess
import os


# Vérifier que les images existent

if not os.path.exists("images/scene1.png"):
    print("❌ Les images des scènes sont introuvables")
    exit()


print("🎬 Création de la vidéo Senghor IA...")


commande = [
    "ffmpeg",
    "-y",
    "-framerate",
    "1",
    "-i",
    "images/scene%d.png",
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    "-vf",
    "scale=1280:720",
    "Senghor_episode.mp4"
]


subprocess.run(commande)


print("✅ Vidéo créée : Senghor_episode.mp4")
