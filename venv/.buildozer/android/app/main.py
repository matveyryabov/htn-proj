import cv2
import kivy.app
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color


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
#        data / data /  # package domain#.#package name#/files/app
        camera.export_to_png("/data/data/org.test.myapp/files/price.png")

        print("Captured")

    pass

class PriceSelectionScreen(Screen):
    pass

class SManager(ScreenManager):
    pass


class Highlight(Widget):
    def __init__(self, **kwargs):
        super(Highlight,self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(1, 0, 0, 0.5, mode="rgba")
                Rectangle(pos=touch.pos,size=(50,50))

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(1, 0, 0, 0.5, mode="rgba")
                Rectangle(pos=touch.pos,size=(50,50))

class GroceryApp(App):
    def build(self):
        sm = SManager()
        return sm

if __name__ == '__main__':
    app = GroceryApp()
    app.run()
