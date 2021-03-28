from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu, RightContent

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class MenuScreen(Screen):
    pass


class ListScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ListScreen(name='list'))
        # sm.switch_to("menu")
        # sm.switch_to(self,"lista",)
        #sm.current = "menu"
        return(sm) 

MyApp().run()
