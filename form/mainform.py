from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

Builder.load_string("""
<MyLayout>
    orientation:"vertical"
    Label:
        id:mylabel
        text:"My App"
    Button:
        text: "Click me"
        on_press: print(mylabel.text)
""")

class MyLayout(BoxLayout):
    pass

class MainFormApp(App):
    def build(self):
        MyLayout()