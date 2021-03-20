from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class DashBoard(Screen):
    pass
class FirstScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("archivokivy.kv")

MyApp().run()
