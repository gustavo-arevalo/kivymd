from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class DashBoard(Screen):
    pass

class FirstScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.title= "mi app"
        self.theme_cls.primary_palette = 'Red'
        return Builder.load_file("main.kv")


MyApp().run()