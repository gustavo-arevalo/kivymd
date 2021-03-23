from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout





class DashBoard(Screen):
    pass


class FirstScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.title = "MI primera app"
        self.theme_cls.primary_pallet = "Red"
        return Builder.load_file("archivo.kv")
MyApp().run()