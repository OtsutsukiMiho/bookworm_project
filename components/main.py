from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
import json
import random
import os

class SoundIcon(ButtonBehavior, Image):
    pass

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_music = SoundLoader.load('sound/main.mp3')
        self.game_music = SoundLoader.load('sound/Ingame.mp3')
        self.volume = 0.25
        self.main_music.play()
        self.main_music.loop = True
        self.volume = 0.25
        self.construct_main_menu()
        
    def on_back_button_pressed_option(self, instance):
        self.main_music.loop = True
        self.main_music.volume = self.volume
        self.construct_main_menu()
        
    def on_back_button_pressed_game(self, instance):
        self.main_music.stop()
        self.main_music.play()
        self.main_music.loop = True
        self.main_music.volume = self.volume
        self.construct_main_menu()
        
    def on_exit_button_pressed(self, instance):
        App.get_running_app().stop()
        
    def on_volume_changed(self, instance, value):
        self.volume = value
        self.main_music.volume = self.volume
        self.game_music.volume = self.volume

    def construct_main_menu(self):

        self.clear_layout()

        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.background_image = Image(source="Image/maxresdefault.jpg")  
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

        self.options_button = Button(text="Options", size_hint=(None, None), size=(200, 60))
        self.options_button.bind(on_press=self.construct_options_menu)
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
        new_back_button.bind(on_press=self.on_back_button_pressed_game)
        new_layout.add_widget(new_back_button)

        self.main_music.stop()
        self.game_music.play()
        self.game_music.loop = True

        self.game_music.play()
        self.game_music.loop = True
        self.game_music.volume = self.volume

        self.question_label = Label(text="", font_size=36, color="black")
        new_layout.add_widget(self.question_label)
        
        self.status_label = Label(text="", font_size=30, color="red")
        new_layout.add_widget(self.status_label)
        
        ui_hp_all = BoxLayout(orientation='vertical', spacing=20, padding=(5, 5))
        new_layout.add_widget(ui_hp_all)
        
        self.ui_hp_enemy = Label(text="Enemy HP: 0", font_size=30, color="red")
        ui_hp_all.add_widget(self.ui_hp_enemy)
        
        self.ui_hp_player = Label(text="Your HP: 0", font_size=30, color="black")
        ui_hp_all.add_widget(self.ui_hp_player)

        self.answer_input = TextInput(hint_text="Type your answer here", multiline=False, font_size=18)
        self.answer_input.bind(on_text_validate=self.check_answer)
        new_layout.add_widget(self.answer_input)

        submit_button = Button(text="Submit Answer", size_hint=(None, None), size=(200, 60))
        submit_button.bind(on_press=self.check_answer)
        new_layout.add_widget(submit_button)
        
        self.current_hp_enemy = 100
        self.current_hp_player = 100
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(current_dir, 'bw_data.json')

        with open(data_file_path, 'r') as file:
            data = json.load(file)
        
        random_index = random.randint(0, len(data['questions']) - 1)

        self.current_question = data['questions'][random_index]['question']
        self.correct_answer = data['questions'][random_index]['answer']
        self.update_question()
        
    def next_question(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(current_dir, 'bw_data.json')
        
        with open(data_file_path, 'r') as file:
            data = json.load(file)
        
        random_index = random.randint(0, len(data['questions']) - 1)

        self.current_question = data['questions'][random_index]['question']
        self.correct_answer = data['questions'][random_index]['answer']
        self.update_question()

    def update_question(self):
        self.ui_hp_player.text = f"Your HP: {self.current_hp_player}"
        self.ui_hp_enemy.text = f"Enemy HP: {self.current_hp_enemy}"
        self.question_label.text = self.current_question
        self.answer_input.text = ""

    def construct_options_menu(self, instance):
        self.clear_layout()

        new_layout = BoxLayout(orientation='vertical', spacing=20, padding=(10, 10))
        new_layout.size_hint = (None, None)
        new_layout.width = self.width
        new_layout.height = self.height
        new_layout.center = self.center
        self.add_widget(new_layout)

        new_title_label = Label(text="Options", font_size=48, color="black")
        new_title_label.size_hint = (None, None)
        new_title_label.size = (self.width, 100)
        new_title_label.center_x = Window.width / 2
        new_title_label.top = Window.height - 50
        self.add_widget(new_title_label)

        self.volume_percentage_label = Label(text=f"Volume : {int(self.volume * 100)}%", font_size=18, color="black")
        self.volume_percentage_label.size_hint = (None, None)
        new_layout.add_widget(self.volume_percentage_label)

        volume_slider = Slider(min=0, max=1, value=self.volume)
        volume_slider.bind(value=self.on_volume_changed)
        new_layout.add_widget(volume_slider)

        sound_icon = SoundIcon(source='Image/speaker-filled-audio-tool.png', size_hint=(None, None), size=(50, 50))
        sound_icon.bind(on_press=self.toggle_sound)
        new_layout.add_widget(sound_icon)

        if self.volume == 0:
            sound_icon.source = 'Image/mute.png'

        new_back_button = Button(text="Back to Main Menu", size_hint=(None, None), size=(200, 60))
        new_back_button.bind(on_press=self.on_back_button_pressed_option)
        new_layout.add_widget(new_back_button)

    def toggle_sound(self, instance):
        if self.volume > 0:
            self.volume = 0
            instance.source = 'Image/mute.png'
        else:
            self.volume = 0.25
            instance.source = 'Image/speaker-filled-audio-tool.png'
        self.main_music.volume = self.volume
        self.game_music.volume = self.volume

    def on_volume_changed(self, instance, value):
        self.volume = value
        self.main_music.volume = self.volume
        self.game_music.volume = self.volume
        self.volume_percentage_label.text = f"Volume : {int(self.volume * 100)}%"    

    def show_status_clear_text(self, instance):
        self.status_label.text = ""

    def check_answer(self, instance):
        user_answer = self.answer_input.text.strip().lower()
        if user_answer == self.correct_answer.lower():
            self.status_label.text = "Correct! Next question..."
            self.status_label.color = "lime"
            Clock.schedule_interval(self.show_status_clear_text, 1)
            self.next_question()
        else:
            self.status_label.text = "Wrong! Try again..."
            self.status_label.color = "red"
            Clock.schedule_interval(self.show_status_clear_text, 1)
        self.update_question()

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()
