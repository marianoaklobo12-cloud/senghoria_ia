from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os
import urllib.parse


class ServeurSenghor(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path.startswith("/creer"):

            dossier = "/home/userland/Senghor_IA/episode_senghor"

            script = os.path.join(
                dossier,
                "montage_musique.sh"
            )

            if os.path.exists(script):

                resultat = subprocess.run(
                    ["bash", script],
                    cwd=dossier,
                    capture_output=True,
                    text=True
                )

                if resultat.returncode == 0:
                    message = "VIDEO_OK"

                else:
                    message = "ERREUR_FFMPEG"

            else:
                message = "SCRIPT_INTROUVABLE"


        else:

            message = "SENGHOR_IA_ACTIF"


        self.send_response(200)

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.end_headers()

        self.wfile.write(
            message.encode()
        )


serveur = HTTPServer(
    ("0.0.0.0", 8080),
    ServeurSenghor
)


print("Serveur Senghor IA actif")

serveur.serve_forever()
