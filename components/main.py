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
        
        self.construct_main_menu()
        
    def on_back_button_pressed(self, instance):
        self.construct_main_menu()
        
    def on_exit_button_pressed(self, instance):
        App.get_running_app().stop()
        
    def construct_main_menu(self):

        self.clear_layout()

        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.background_image = Image(source="maxresdefault.jpg")  
        self.add_widget(self.background_image)
        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.pos = (0, 0)
        self.background_image.size = (Window.width, Window.height)
        
        self.title_label = Label(text="Bookworm Adventures", font_size=48, color="black")
        self.title_label.size_hint = (None, None)
        self.title_label.size = (self.width, 100)
        self.title_label.center_x = Window.width / 2
        self.title_label.top = Window.height - 50
        self.add_widget(self.title_label)
        
        layout = BoxLayout(orientation='vertical', spacing=20, padding=(10, 10))
        layout.size_hint = (None, None)
        layout.width = self.width  
        layout.height = self.height  
        layout.center = self.center
        self.add_widget(layout)
        
        self.play_button = Button(text="Play", size_hint=(None, None), size=(200, 60))
        self.play_button.bind(on_press=self.construct_game_menu)
        layout.add_widget(self.play_button)
        
        self.options_button = Button(text="Exit", size_hint=(None, None), size=(200, 60))
        self.options_button.bind(on_press=self.on_exit_button_pressed)
        layout.add_widget(self.options_button)

    def clear_layout(self):
        for widget in self.children[:]:
            if isinstance(widget, BoxLayout):
                self.remove_widget(widget)
                self.remove_widget(self.title_label)

    def construct_game_menu(self, instance):

        self.clear_layout()

        new_layout = BoxLayout(orientation='vertical', spacing=20, padding=(10, 10))
        new_layout.size_hint = (None, None)
        new_layout.width = self.width  
        new_layout.height = self.height  
        new_layout.center = self.center
        self.add_widget(new_layout)
        
        new_title_label = Label(text="Game Started!", font_size=48, color="black")
        new_title_label.size_hint = (None, None)
        new_title_label.size = (self.width, 100)
        new_title_label.center_x = Window.width / 2
        new_title_label.top = Window.height - 50
        self.add_widget(new_title_label)
        
        new_back_button = Button(text="Back to Main Menu", size_hint=(None, None), size=(200, 60))
        new_back_button.bind(on_press=self.on_back_button_pressed)
        new_layout.add_widget(new_back_button)

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()
