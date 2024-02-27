from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.image import Image

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.background_image = Image(source="maxresdefault.jpg")  
        self.add_widget(self.background_image)

        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.pos = (0, 0)
        self.background_image.size = (Window.width, Window.height)
        
        layout = BoxLayout(orientation='vertical', spacing=20)
        layout.size_hint = (None, None)
        layout.width = self.width  
        layout.height = self.height  
        layout.pos = (Window.width - self.width) / 2, (Window.height - self.height) / 2
        self.add_widget(layout)
        
        self.title_label = Label(text="Bookworm Adventures", font_size=48)
        layout.add_widget(self.title_label)
        
        self.play_button = Button(text="Play")
        self.play_button.bind(on_press=self.on_play_button_pressed)  
        layout.add_widget(self.play_button)
        
        self.options_button = Button(text="Options")
        layout.add_widget(self.options_button)

    def on_play_button_pressed(self, instance):

        self.clear_widgets()  
        
        
        new_layout = BoxLayout(orientation='vertical', spacing=20)
        new_layout.size_hint = (None, None)
        new_layout.width = self.width  
        new_layout.height = self.height  
        new_layout.pos = (Window.width - self.width) / 2, (Window.height - self.height) / 2
        self.add_widget(new_layout)
        
        new_title_label = Label(text="Game Started!", font_size=48)
        new_layout.add_widget(new_title_label)
        
        new_back_button = Button(text="Back to Main Menu")
        new_back_button.bind(on_press=self.on_back_button_pressed)  
        new_layout.add_widget(new_back_button)

    def on_back_button_pressed(self, instance):

        self.clear_widgets()  
        self.__init__()  


class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()