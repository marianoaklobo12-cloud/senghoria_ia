import os
from PIL import Image, ImageDraw, ImageFont


DOSSIER = "episode_senghor"


def creer_images_ia(scenes):

    os.makedirs(
        DOSSIER,
        exist_ok=True
    )


    print("🖼️ Création des images IA...")



    for scene in scenes:


        numero = scene["numero"]

        titre = scene["titre"]

        description = scene["description"]



        image = Image.new(
            "RGB",
            (1280,720),
            (10,20,50)
        )


        dessin = ImageDraw.Draw(image)



        texte = (

            "SENGHOR IA\n\n"

            f"SCENE {numero}\n\n"

            f"{titre}\n\n"

            f"{description}"

        )



        dessin.text(

            (80,120),

            texte,

            fill=(0,220,255)

        )



        chemin = (

            f"{DOSSIER}/scene{numero}.png"

        )



        image.save(chemin)



        print(
            "✅ Image créée :",
            chemin
        )



    print(
        "🚀 Images IA terminées"
    )
