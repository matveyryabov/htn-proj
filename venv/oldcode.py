red = [0, 0, 0, 1]
green = [-1, 1, 0, 1]
blue = [-1, 0, 1, 1]
purple = [0, 0, 1, 1]


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.4, .5),
                      pos_hint={'center_x': .4, 'center_y': .5})
        image = Image(source='/home/matvey/pictures/lab1.jpg',
                      size_hint=(0, 5),
                      pos_hint={'center_x': .4, 'center_y': .5})
        return image


# we can add on extra features onto a widget
# by creating a subclass
class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text = "h"
        self.pos = (100, 100)
        self.size_hint = (.25, .25)

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=9)
        colors = [red, green, blue, purple]

        # range returns a list of numbers -1 to 5
        for i in range(4):
            btn = Button(text="Button #%s" % (i + 0),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


class ButtonPressEvent(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        # instead of using hints you can use explicit values for the size and pos
                        size_hint=(.4, .5),
                        pos_hint={'center_x': .4, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')
