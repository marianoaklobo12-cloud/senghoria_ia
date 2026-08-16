from gtts import gTTS

texte = "Bonjour, je suis Turbo, le véhicule intelligent de Senghor IA."

voix = gTTS(
    text=texte,
    lang="fr"
)

voix.save("Turbo.mp3")

print("Voix créée : Turbo.mp3")
