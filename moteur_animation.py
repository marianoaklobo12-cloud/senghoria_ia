import os
import subprocess


dossier = "images"
sortie = "Senghor_animation.mp4"


print("🎬 Démarrage moteur animation Senghor IA...")


fichiers = []

for i in range(1,9):
    image = f"{dossier}/scene{i}.png"
    if os.path.exists(image):
        fichiers.append(image)


if len(fichiers) == 0:
    print("❌ Aucune image trouvée")
    exit()


liste = "liste_images.txt"

with open(liste,"w") as f:
    for img in fichiers:
        f.write(f"file '{img}'\n")
        f.write("duration 10\n")

    f.write(f"file '{fichiers[-1]}'\n")


commande = [
    "ffmpeg",
    "-y",
    "-f",
    "concat",
    "-safe",
    "0",
    "-i",
    liste,
    "-vf",
    "scale=1280:720,zoompan=z='min(zoom+0.0015,1.15)':d=240:s=1280x720:fps=24",
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    "-r",
    "24",
    sortie
]


subprocess.run(commande)


print("✅ Animation créée :", sortie)
