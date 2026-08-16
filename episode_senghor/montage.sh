#!/bin/bash

ffmpeg -y \
-loop 1 -i scene1.png \
-loop 1 -i scene2.png \
-loop 1 -i scene3.png \
-loop 1 -i scene4.png \
-loop 1 -i scene5.png \
-loop 1 -i scene6.png \
-loop 1 -i scene7.png \
-loop 1 -i scene8.png \
-i voix1.mp3 \
-i voix2.mp3 \
-i voix3.mp3 \
-i voix4.mp3 \
-i voix5.mp3 \
-i voix6.mp3 \
-i voix7.mp3 \
-i voix8.mp3 \
-filter_complex "
[0:v]scale=1280:720[v0];
[1:v]scale=1280:720[v1];
[2:v]scale=1280:720[v2];
[3:v]scale=1280:720[v3];
[4:v]scale=1280:720[v4];
[5:v]scale=1280:720[v5];
[6:v]scale=1280:720[v6];
[7:v]scale=1280:720[v7];
[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[outv]
" \
-map "[outv]" \
-map 8:a \
-c:v libx264 \
-c:a aac \
-shortest \
Senghor_episode_final.mp4
