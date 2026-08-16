#!/bin/bash

DUREE=${1:-10}

echo "🎬 Création vidéo Senghor IA : $DUREE secondes par scène"

rm -f scene*.mp4 liste.txt Senghor_TikTok_final.mp4

for i in {1..8}
do
ffmpeg -y \
-loop 1 \
-i scene$i.png \
-t $DUREE \
-r 25 \
-vf "scale=1080:1920" \
-c:v libx264 \
-pix_fmt yuv420p \
scene$i.mp4
done


for i in {1..8}
do
echo "file 'scene$i.mp4'" >> liste.txt
done


ffmpeg -y \
-f concat \
-safe 0 \
-i liste.txt \
-i musique.mp3 \
-c:v copy \
-c:a aac \
-shortest \
Senghor_TikTok_final.mp4


echo "✅ Vidéo terminée : Senghor_TikTok_final.mp4"
