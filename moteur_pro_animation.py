import os
import subprocess
import random

print("🎬 Senghor IA - Moteur animation PRO V2")

DOSSIER_IMAGES = "images"
DOSSIER_AUDIO = "audio"

VIDEO_CAMERA = "animation_camera.mp4"
VIDEO_FINAL = "Senghor_video_finale.mp4"

# Préparation images
images = sorted([
    f for f in os.listdir(DOSSIER_IMAGES)
    if f.endswith(".png") or f.endswith(".jpg")
])

if not images:
    print("❌ Aucune image trouvée")
    exit()

print("📸 Images trouvées :", len(images))


# Création liste ffmpeg
with open("liste_images.txt","w") as f:
    for img in images:
        chemin = os.path.abspath(
            os.path.join(DOSSIER_IMAGES,img)
        )
        f.write(f"file '{chemin}'\n")
        f.write("duration 5\n")


# Animation caméra avec zoom
cmd = [
"ffmpeg",
"-y",
"-f","concat",
"-safe","0",
"-i","liste_images.txt",
"-vf",
"scale=1280:720,zoompan=z='min(zoom+0.0015,1.5)':d=125:s=1280x720",
"-r","24",
VIDEO_CAMERA
]

subprocess.run(cmd)

print("🎥 Animation caméra créée")


# Recherche voix
voix = None

if os.path.exists(DOSSIER_AUDIO):
    for f in os.listdir(DOSSIER_AUDIO):
        if f.endswith(".mp3"):
            voix = os.path.join(DOSSIER_AUDIO,f)
            break


if voix:

    print("🎤 Voix trouvée :", voix)

    cmd2=[
    "ffmpeg",
    "-y",
    "-i",
    VIDEO_CAMERA,
    "-i",
    voix,
    "-shortest",
    "-c:v",
    "copy",
    "-c:a",
    "aac",
    VIDEO_FINAL
    ]

    subprocess.run(cmd2)

    print("✅ Vidéo finale avec voix créée :",VIDEO_FINAL)

else:

    os.rename(VIDEO_CAMERA,VIDEO_FINAL)
    print("⚠️ Pas de voix trouvée, vidéo créée sans audio")


print("🎉 Senghor IA terminé")
