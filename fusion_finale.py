import subprocess

print("🎬 Fusion vidéo + voix longue...")


commande = [
    "ffmpeg",
    "-y",
    "-i",
    "Senghor_episode_long.mp4",
    "-i",
    "audio/robot_longue.mp3",
    "-map",
    "0:v",
    "-map",
    "1:a",
    "-c:v",
    "copy",
    "-c:a",
    "aac",
    "-shortest",
    "Senghor_episode_final.mp4"
]


subprocess.run(commande)


print("✅ Épisode final créé : Senghor_episode_final.mp4")
