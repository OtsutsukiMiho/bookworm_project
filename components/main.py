from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.canvas.clear()
        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=(0, 0), size=(self.width, self.height))

        self.title_label = Label(text="Bookworm Adventures", font_size=48, pos=(100, 100))
        self.add_widget(self.title_label)

        self.play_button = Button(text="Play", pos=(200, 200))
        self.add_widget(self.play_button)

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()