from PIL import Image, ImageDraw
import os


def creer_scene(texte, numero):

    if not os.path.exists("images"):
        os.makedirs("images")


    image = Image.new(
        "RGB",
        (1280,720),
        (15,35,80)
    )


    dessin = ImageDraw.Draw(image)


    dessin.text(
        (100,300),
        "Senghor IA\n\nScene "+str(numero)+"\n\n"+texte,
        fill=(255,255,255)
    )


    fichier = f"images/scene{numero}.png"

    image.save(fichier)

    print("✅ Créée :", fichier)



scenes = [

"Turbo arrive dans la ville futuriste",

"Titan construit les bâtiments",

"Luna explore le ciel",

"Les robots travaillent ensemble",

"La ville devient moderne",

"Les véhicules célèbrent la réussite",

"Une nouvelle aventure commence",

"Senghor IA termine l'épisode"

]


for i, scene in enumerate(scenes,1):

    creer_scene(scene,i)
