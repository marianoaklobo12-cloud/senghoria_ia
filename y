from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window


Window.clearcolor = (0.03, 0.05, 0.12, 1)


class Carte(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.05, 0.12, 0.25, 1)
        self.color = (0.5, 0.8, 1, 1)


class SenghorAccueil(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical",
                         spacing=15,
                         padding=20,
                         **kwargs)

        # En-tête
        haut = BoxLayout(size_hint_y=0.15)

        titre = Label(
            text="[b]Senghor[/b]\nStudio de création vidéo IA",
            markup=True,
            font_size=24,
            color=(0.2,0.8,1,1)
        )

        connexion = Button(
            text="🔒 Connexion / Inscription",
            size_hint_x=0.4,
            background_color=(0.05,0.15,0.3,1)
        )

        haut.add_widget(titre)
        haut.add_widget(connexion)

        self.add_widget(haut)


        # Zone description vidéo
        zone = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=0.35
        )

        self.video = TextInput(
            hint_text="Décris ta vidéo...",
            multiline=True,
            background_color=(0.08,0.12,0.25,1),
            foreground_color=(1,1,1,1)
        )

        creer = Button(
            text="🎬  CRÉER UNE VIDÉO",
            size_hint_y=0.3,
            background_color=(0,0.7,1,1)
        )

        zone.add_widget(self.video)
        zone.add_widget(creer)

        self.add_widget(zone)


        # Cartes principales
        grille = GridLayout(
            cols=2,
            spacing=12,
            size_hint_y=0.35
        )

        boutons = [
            ("🤖 Assistant IA\nCréer scénarios"),
            ("🎬 Mes vidéos\nVoir mes créations"),
            ("📁 Mes projets\nSauvegarder histoires"),
            ("⚙ Paramètres\nConfiguration")
        ]

        for b in boutons:
            grille.add_widget(Carte(text=b))

        self.add_widget(grille)


        # Barre du bas
        bas = GridLayout(
            cols=4,
            size_hint_y=0.12
        )

        for nom in ["🏠 Accueil",
                    "✨ Créer",
                    "🎥 Vidéos",
                    "👤 Compte"]:
            bas.add_widget(
                Button(
                    text=nom,
                    background_color=(0.05,0.1,0.2,1)
                )
            )

        self.add_widget(bas)



class SenghorApp(App):
    def build(self):
        return SenghorAccueil()


if __name__ == "__main__":
    SenghorApp().run()
