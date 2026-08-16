import subprocess

print("🎬 Création épisode long Senghor IA...")


commande = [
    "ffmpeg",
    "-y",
    "-framerate",
    "0.1",
    "-i",
    "images/scene%d.png",
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    "-vf",
    "scale=1280:720",
    "Senghor_episode_long.mp4"
]


subprocess.run(commande)

print("✅ Vidéo longue créée : Senghor_episode_long.mp4")
