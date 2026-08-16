from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle, Rectangle


class StyleButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_color = (0,0,0,0)

        with self.canvas.before:
            Color(0.05,0.35,0.65,1)

            self.rect = RoundedRectangle(
                radius=[25],
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )


    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size



class Accueil(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        with self.canvas.before:

            Color(
                0.03,
                0.06,
                0.15,
                1
            )

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )


        self.bind(
            pos=self.update_background,
            size=self.update_background
        )


        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )


        titre = Label(
            text="🚀 Senghor IA\nStudio de création vidéo IA",
            font_size=30
        )


        self.description = TextInput(
            hint_text="Décris ta vidéo...",
            multiline=False,
            size_hint_y=0.15
        )


        creer = StyleButton(
            text="▶️ Lancer la création",
            size_hint_y=0.18
        )


        menu = GridLayout(
            cols=2,
            spacing=20,
            size_hint_y=0.4
        )


        pages = [
            ("🤖 Assistant IA","assistant"),
            ("🎬 Vidéos","videos"),
            ("📁 Projets","projets"),
            ("⚙️ Paramètres","parametres")
        ]
        for texte, page in pages:

            bouton = StyleButton(
                text=texte
            )

            bouton.bind(
                on_press=lambda x,p=page:
                setattr(
                    self.manager,
                    "current",
                    p
                )
            )

            menu.add_widget(bouton)


        layout.add_widget(titre)
        layout.add_widget(self.description)
        layout.add_widget(creer)
        layout.add_widget(menu)


        self.add_widget(layout)



    def update_background(self,*args):

        self.background.pos = self.pos
        self.background.size = self.size




class Page(Screen):

    def __init__(self, titre, **kwargs):

        super().__init__(**kwargs)


        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )


        retour = StyleButton(
            text="⬅️ Retour",
            size_hint_y=0.15
        )


        retour.bind(
            on_press=lambda x:
            setattr(
                self.manager,
                "current",
                "accueil"
            )
        )


        label = Label(
            text=titre,
            font_size=35
        )


        layout.add_widget(retour)
        layout.add_widget(label)


        self.add_widget(layout)




class SenghorApp(App):

    def build(self):

        sm = ScreenManager()


        sm.add_widget(
            Accueil(
                name="accueil"
            )
        )


        sm.add_widget(
            Page(
                "🤖 Assistant IA",
                name="assistant"
            )
        )


        sm.add_widget(
            Page(
                "🎬 Mes vidéos",
                name="videos"
            )
        )


        sm.add_widget(
            Page(
                "📁 Mes projets",
                name="projets"
            )
        )


        sm.add_widget(
            Page(
                "⚙️ Paramètres",
                name="parametres"
            )
        )


        return sm




if __name__ == "__main__":

    SenghorApp().run()
