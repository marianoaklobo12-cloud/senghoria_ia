from gtts import gTTS
import os


def creer_voix(
    texte,
    style="robot calme",
    langue="fr"
):


    os.makedirs(
        "audio",
        exist_ok=True
    )


    styles = {


        "robot calme":
        "Bonjour, je suis Senghor IA. Je vais raconter cette histoire calmement.",


        "robot joyeux":
        "Super ! Une nouvelle aventure commence avec beaucoup de joie !",


        "robot amusant":
        "Haha ! Prépare-toi pour une aventure drôle et incroyable !",


        "robot géant":
        "Attention ! Le grand robot arrive pour accomplir une mission énorme !",


        "robot énergique":
        "C'est parti ! L'action commence maintenant !",


        "robot cinéma":
        "Dans un monde extraordinaire, une nouvelle histoire va commencer."


    }



    introduction = styles.get(

        style,

        styles["robot calme"]

    )



    contenu = (

        introduction

        + "\n\n"

        + texte

    )



    fichier = (

        "audio/"

        + style.replace(" ","_")

        + ".mp3"

    )



    voix = gTTS(

        text=contenu,

        lang=langue,

        slow=False

    )


    voix.save(fichier)



    print(
        "🎙 Voix créée :",
        fichier
    )



    return fichier
