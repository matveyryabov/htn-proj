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
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("price.png".format(timestr))

        print("Captured")

    pass

class PriceSelectionScreen(Screen):
    pass

class SManager(ScreenManager):
    pass

class GroceryApp(App):
    def build(self):
        sm = SManager()
        return sm

if __name__ == '__main__':
    app = GroceryApp()
    app.run()
