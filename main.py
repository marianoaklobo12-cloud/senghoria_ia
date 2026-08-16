from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


Window.clearcolor = (0.03, 0.05, 0.12, 1)


class Carte(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.05, 0.12, 0.25, 1)
        self.color = (0.5, 0.8, 1, 1)


class ParametresPage(BoxLayout):

    def __init__(self, retour, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=10,
            padding=20,
            **kwargs
        )

        titre = Label(
            text="[b]⚙ PARAMÈTRES SENGHOR IA[/b]",
            markup=True,
            font_size=24,
            color=(0.2,0.8,1,1),
            size_hint_y=0.12
        )

        self.add_widget(titre)

        scroll = ScrollView()

        liste = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None
        )

        liste.bind(minimum_height=liste.setter("height"))

        options = [
            "👤 Profil utilisateur",
            "🎨 Apparence",
            "🤖 Intelligence Artificielle",
            "🎙️ Voix IA",
            "🎬 Vidéo",
            "🎵 Audio",
            "📁 Stockage",
            "🔐 Compte",
            "🌐 Réseau",
            "ℹ️ À propos"
        ]

        for option in options:
            bouton = Button(
                text=option,
                size_hint_y=None,
                height=60,
                background_color=(0.05,0.15,0.3,1)
            )
            liste.add_widget(bouton)

        scroll.add_widget(liste)
        self.add_widget(scroll)


        retour_btn = Button(
            text="⬅ Retour Accueil",
            size_hint_y=0.12
        )

        retour_btn.bind(on_press=retour)

        self.add_widget(retour_btn)



class SenghorAccueil(BoxLayout):

    def __init__(self, changer_page, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )

        titre = Label(
            text="[b]Senghor IA[/b]\nStudio de création vidéo IA",
            markup=True,
            font_size=24,
            color=(0.2,0.8,1,1)
        )

        self.add_widget(titre)


        self.video = TextInput(
            hint_text="Décris ta vidéo...",
            multiline=True,
            size_hint_y=0.25
        )

        self.add_widget(self.video)


        creer = Button(
            text="🎬 CRÉER UNE VIDÉO",
            size_hint_y=0.15
        )

        self.add_widget(creer)


        grille = GridLayout(
            cols=2,
            spacing=10
        )


        param = Carte(
            text="⚙ Paramètres"
        )

        param.bind(
            on_press=lambda x: changer_page("param")
        )


        boutons = [
            "🤖 Assistant IA",
            "🎙️ Voix IA",
            "🎥 Mes vidéos",
            "📁 Mes projets"
        ]


        for b in boutons:
            grille.add_widget(
                Carte(text=b)
            )


        grille.add_widget(param)

        self.add_widget(grille)



class SenghorApp(App):

    def build(self):

        self.accueil = SenghorAccueil(
            self.changer_page
        )

        return self.accueil


    def changer_page(self, page):

        if page == "param":

            self.root.clear_widgets()

            self.root.add_widget(
                ParametresPage(
                    self.retour_accueil
                )
            )


    def retour_accueil(self, instance):

        self.root.clear_widgets()

        self.root.add_widget(
            self.accueil
        )



if __name__ == "__main__":
    SenghorApp().run()
