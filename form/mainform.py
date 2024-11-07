from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyLayout(BoxLayout):
    pass


class MainFormApp(App):
    def build(self):
        return MyLayout()
