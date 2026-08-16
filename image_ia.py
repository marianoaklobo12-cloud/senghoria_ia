from PIL import Image, ImageDraw
import os


def creer_image(description, numero):

    dossier = "images"

    if not os.path.exists(dossier):
        os.makedirs(dossier)

    largeur = 1280
    hauteur = 720

    image = Image.new(
        "RGB",
        (largeur, hauteur),
        (15, 35, 80)
    )

    dessin = ImageDraw.Draw(image)

    texte = "Senghor IA\n\n" + description

    dessin.text(
        (100, 250),
        texte,
        fill=(255,255,255)
    )

    fichier = f"{dossier}/scene{numero}.png"

    image.save(fichier)

    print("🖼️ Image créée :", fichier)


# Lecture automatique du prompt
if os.path.exists("texte_scene.txt"):

    with open("texte_scene.txt","r",encoding="utf-8") as f:
        description = f.read()

else:
    description = "Une scène de film IA"


# Création de plusieurs scènes
for i in range(1,6):
    creer_image(description, i)


print("✅ Images générées automatiquement")
