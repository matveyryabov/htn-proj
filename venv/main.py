import kivy.app
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
import cv2

#
CURSOR_SIZE = 20
##(368, 207)

class SManager(ScreenManager):
    pass

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
        camera.export_to_png("price.png")
        print("Captured")
    pass

class Highlight(Widget):
    def __init__(self, **kwargs):
        super(Highlight,self).__init__(**kwargs)

        Window.bind(on_resize=self.on_window_resize)

        self.IMAGE_HEIGHT, self.IMAGE_WIDTH, dummy_var = cv2.imread('price.png').shape

        self.size = (self.IMAGE_WIDTH - CURSOR_SIZE,self.IMAGE_HEIGHT - CURSOR_SIZE)
        self.pos = (Window.width/2 - self.IMAGE_WIDTH/2 + CURSOR_SIZE/2,Window.height/2 - self.IMAGE_HEIGHT/2 + CURSOR_SIZE/2)

        with self.canvas:
            Color(1, 1, 1, 0.5, mode="rgba")
            Rectangle(pos=self.pos,size=self.size)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(1, 0, 0, 0.5, mode="rgba")
                Rectangle(pos=(touch.pos[0] - CURSOR_SIZE/2, touch.pos[1] - CURSOR_SIZE/2),size=(CURSOR_SIZE,CURSOR_SIZE))

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            print(touch.pos)
            with self.canvas:
                Color(1, 0, 0, 0.5, mode="rgba")
                Rectangle(pos=(touch.pos[0] - CURSOR_SIZE/2, touch.pos[1] - CURSOR_SIZE/2),size=(CURSOR_SIZE,CURSOR_SIZE))

    def on_window_resize(self, window, width, height):
        self.pos = (Window.width/2 - self.IMAGE_WIDTH/2 + CURSOR_SIZE/2,Window.height/2 - self.IMAGE_HEIGHT/2 + CURSOR_SIZE/2)
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 0.5, mode="rgba")
            Rectangle(pos=self.pos,size=self.size)


class PriceSelectionScreen(Screen):
    pass

class GroceryApp(App):
    def build(self):
        sm = SManager()
        return sm

if __name__ == '__main__':
    # app = MainApp()
    # app = HBoxLayoutExample()
    # app = ButtonPressEvent()
    app = GroceryApp()
    app.run()
