from kivy.app import App
from kivy.uix.label import Label

class MainFormApp(App):
    def build(self):
        l1 = Label(text="Hello World", font_size=50)
        return l1