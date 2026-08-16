import os
import subprocess
import time

print("🤖 Senghor IA - Moteur complet")
print("================================")


# 1 - Demande du prompt utilisateur

prompt = input("\n📝 Décris ta vidéo : ")

if prompt.strip() == "":
    print("❌ Aucun texte reçu")
    exit()


print("\n🎬 Création du scénario...")

with open("texte_scene.txt","w",encoding="utf-8") as f:
    f.write(prompt)


# 2 - Génération des images

print("\n📸 Génération des images...")

if os.path.exists("image_ia.py"):
    subprocess.run(
        ["python3","image_ia.py"]
    )
else:
    print("⚠️ image_ia.py absent")


# 3 - Création voix

print("\n🎤 Création de la voix...")

if os.path.exists("voix_robot.py"):
    subprocess.run(
        ["python3","voix_robot.py"]
    )
else:
    print("⚠️ voix_robot.py absent")


# 4 - Animation caméra

print("\n🎥 Animation caméra...")

if os.path.exists("moteur_pro_animation.py"):
    subprocess.run(
        ["python3","moteur_pro_animation.py"]
    )
else:
    print("⚠️ moteur_pro_animation.py absent")


# 5 - Vérification résultat

print("\n🔎 Recherche vidéo finale...")


videos = [
"Senghor_video_finale.mp4",
"Senghor_animation_pro.mp4",
"Senghor_animation.mp4"
]


for video in videos:
    if os.path.exists(video):
        print("\n✅ Vidéo créée :",video)
        break
else:
    print("\n❌ Aucune vidéo trouvée")


print("\n🎉 Senghor IA terminé !")
