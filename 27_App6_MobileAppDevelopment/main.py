from kivy.app import App
from kivy.lang import Builder # odgovoran za povezivanje py i kv fajlova
from kivy.uix.screenmanager import  ScreenManager, Screen
from yaml import load

Builder.load_file('design.kv')