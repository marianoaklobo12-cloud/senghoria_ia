#!/bin/bash

echo "🎬 Montage Senghor IA en cours..."

# Création des 8 scènes avec images + voix

for i in {1..8}
do

ffmpeg -y \
-loop 1 \
-i scene$i.png \
-i voix$i.mp3 \
-t 10 \
-vf "scale=1280:720" \
-c:v libx264 \
-c:a aac \
-shortest \
scene_video$i.mp4

done


echo "🔗 Assemblage des scènes..."

rm -f liste.txt

for i in {1..8}
do
echo "file 'scene_video$i.mp4'" >> liste.txt
done


ffmpeg -y \
-f concat \
-safe 0 \
-i liste.txt \
-c copy \
Senghor_episode_test.mp4


echo "✅ Vidéo terminée : Senghor_episode_test.mp4"
