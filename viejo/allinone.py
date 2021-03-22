from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button: 
            text: 'Otra Pantalla'
            on_press: root.manager.current = 'otrapantalla'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
    BoxLayout:
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<OtraPantalla>:
    BoxLayout:
        Label:
            text: "hola etiqueta"
        Label
            text: "Otro label"
        Button:
            text: "Que boton!"
            on_press: root.manager.current = 'settings'
""")

# Declare both screens

class OtraPantalla(Screen):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestoApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(OtraPantalla(name='otrapantalla'))
        return sm

if __name__ == '__main__':
    TestoApp().run()