from kivy.app import App
from kivy.lang import Builder # odgovoran za povezivanje py i kv fajlova
from kivy.uix.screenmanager import  ScreenManager, Screen
from yaml import load

Builder.load_file('design.kv')

class LoginScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()  # sa () mi inicijaliziramo metod!!
    
if __name__ == "__main__":
    MainApp().run()