

rm buildozer.spec

cat > buildozer.spec <<'EOF'
[app]

title = Senghor

package.name = senghor
package.domain = org.senghor

source.dir = .

source.include_exts = py,png,jpg,jpeg,mp3,wav,mp4,json

version = 1.0

requirements = python3,kivy,pillow,gtts,moviepy,imageio,imageio-ffmpeg

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 35

android.minapi = 23

android.archs = arm64-v8a


[buildozer]

log_level = 2

warn_on_root = 0
EOF
