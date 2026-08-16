import subprocess


commande = [
    "ffmpeg",
    "-y",
    "-i",
    "Senghor_episode_long.mp4",
    "-i",
    "audio/robot_futuriste.mp3",
    "-map",
    "0:v",
    "-map",
    "1:a",
    "-c:v",
    "copy",
    "-c:a",
    "aac",
    "-b:a",
    "128k",
    "-t",
    "80",
    "Senghor_episode_final.mp4"
]


subprocess.run(commande)


print("✅ Vidéo finale créée : Senghor_episode_final.mp4")
