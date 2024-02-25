from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.canvas.clear()
        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=(0, 0), size=(1920, 1080))

        layout = BoxLayout(orientation='vertical', spacing=20)
        self.add_widget(layout)

        self.title_label = Label(text="Bookworm Adventures", font_size=48)
        layout.add_widget(self.title_label)

        self.play_button = Button(text="Play")
        layout.add_widget(self.play_button)

        self.options_button = Button(text="Options")
        layout.add_widget(self.options_button)

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()
