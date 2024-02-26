from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.lang import Builder
from kivy import Image
class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_image = Image(source="/user/Boony/ดาวน์โหลด/maxresdefault", pos=self.pos, size=self.size)
        self.add_widget(self.background_image, insert=0)  # แทรกที่ด้านล่าง

        with self.canvas.before:
            Color(1, 1, 1)  
            self.background_image = Rectangle(pos=self.pos, size=self.size)
        
        self.canvas.clear()
        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height))
        
        layout = BoxLayout(orientation='vertical', spacing=20)
        layout.size_hint = (None, None)
        layout.width = self.width  # Set layout width to widget width
        layout.height = self.height  # Set layout height to widget height
        layout.pos = (Window.width - self.width) / 2, (Window.height - self.height) / 2
        self.add_widget(layout)
        
        self.title_label = Label(text="Bookworm Adventures", font_size=48)
        layout.add_widget(self.title_label)
        
        self.play_button = Button(text="Play")
        layout.add_widget(self.play_button)
        
        self.options_button = Button(text="Options")
        layout.add_widget(self.options_button)


    def on_size(self, instance, width, height):
        self.background_image.pos = self.pos
        self.background_image.size = self.size

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()
