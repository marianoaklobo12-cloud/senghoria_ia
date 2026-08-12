from kivy.app import App
from kivy.uix.label import Label

class SenghorIA(App):
    def build(self):
        return Label(text="Senghor IA - Createur de films IA")

if __name__ == "__main__":
    SenghorIA().run()
