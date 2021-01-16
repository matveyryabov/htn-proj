import random
import time
import kivy.app
from kivy.app import App
import logging
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#Logger.setLevel(logging.TRACE)

class MenuScreen(Screen):
    pass

class QueryScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class GroceryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(QueryScreen(name='query'))
        sm.add_widget(AddScreen(name='add'))
        return sm

if __name__ == '__main__':
    # app = MainApp()
    # app = HBoxLayoutExample()
    # app = ButtonPressEvent()
    GroceryApp().run()
