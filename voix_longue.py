import subprocess

print("🎙️ Création voix longue...")


commande = [
    "ffmpeg",
    "-y",
    "-stream_loop",
    "12",
    "-i",
    "audio/robot_futuriste.mp3",
    "-t",
    "80",
    "audio/robot_longue.mp3"
]


subprocess.run(commande)

print("✅ Voix longue créée")
