from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import urllib.parse
import os


DOSSIER = "/home/userland/Senghor_IA/episode_senghor"


class ServeurSenghor(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urllib.parse.urlparse(self.path)

        if url.path == "/creer":

            parametres = urllib.parse.parse_qs(url.query)

            duree = parametres.get(
                "duree",
                ["10"]
            )[0]


            print(
                "🎬 Création vidéo durée :",
                duree,
                "secondes"
            )


            script = os.path.join(
                DOSSIER,
                "montage_musique.sh"
            )


            try:

                resultat = subprocess.run(
                    [
                        "bash",
                        script,
                        duree
                    ],
                    cwd=DOSSIER,
                    capture_output=True,
                    text=True
                )


                if resultat.returncode == 0:

                    reponse = "VIDEO_OK"

                else:

                    reponse = resultat.stderr


            except Exception as e:

                reponse = str(e)


            self.send_response(200)

            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )

            self.end_headers()

            self.wfile.write(
                reponse.encode()
            )


        else:

            self.send_response(404)

            self.end_headers()



serveur = HTTPServer(
    ("0.0.0.0",8080),
    ServeurSenghor
)


print("Serveur Senghor IA actif")


serveur.serve_forever()
