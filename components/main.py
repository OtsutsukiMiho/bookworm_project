from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.metrics import dp
import json
import random
import os

class SoundIcon(ButtonBehavior, Image):
    pass

class MainMenuBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.background_image = Image(source="Image/maxresdefault.jpg")
        self.add_widget(self.background_image)
        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.pos = (0, 0)
        self.background_image.size = (Window.width, Window.height)

class GameMenuBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.background_image = Image(source="Image/ingame.jpg")
        self.add_widget(self.background_image)
        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.pos = (0, 0)
        self.background_image.size = (Window.width, Window.height)

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        LabelBase.register(name='8bit',
                           fn_regular='fonts/TA 8 bit.otf')
        self.main_music = SoundLoader.load('sound/main.mp3')
        self.game_music = SoundLoader.load('sound/GameBGM.mp3')
        self.main_music.loop = True
        self.game_music.loop = True
        self.volume = 0.25
        self.main_music.play()
        self.game_music.play()
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

        main_menu_background = MainMenuBackground()
        self.add_widget(main_menu_background)

        with self.canvas:
            Color(1, 1, 1, 0)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.background_image = Image(source="Image/maxresdefault.jpg")  
        self.add_widget(self.background_image)
        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.pos = (0, 0)
        self.background_image.size = (Window.width, Window.height)
        
        self.game_music.stop()
        self.main_music.play()
        self.main_music.volume = self.volume
        self.game_music.volume = self.volume
        
        self.title_label = Label(text="Bookworm Adventures", font_name='8bit', font_size=70, color=(1, 0.6, 0, 1), bold=True, outline_color=(0, 0, 0, 1), outline_width=2)
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

    def construct_game_menu(self, popup_instance=None):
        self.clear_layout()

        game_menu_background = GameMenuBackground()
        self.add_widget(game_menu_background)

        self.main_music.stop()
        self.game_music.play()
        self.main_music.volume = self.volume
        self.game_music.volume = self.volume

        gg_popup = Popup(title='', size_hint=(None, None), size=(400, 200))
        gg_popup.background_color = (0, 0, 0, 0)  

        game_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        game_content_layout = BoxLayout(orientation='vertical', spacing=10)

        game_start_label = Label(text="Game Start!", font_size=36, color=[1, 0.6, 0, 1])

        game_content_layout.add_widget(game_start_label)
        game_content_layout.add_widget(game_layout)

        gg_popup.content = game_content_layout

        gg_popup.open()
        Clock.schedule_once(gg_popup.dismiss, 1)
        
        top_layout = BoxLayout(orientation='vertical', spacing=20, padding=(10, 10))
        top_layout.size_hint = (None, None)
        top_layout.width = self.width  
        top_layout.height = self.height * 0.8  
        top_layout.center = self.center

        top_title_label = Label(text="Bookworm Adventures", font_name='8bit', font_size=55, color=(1, 0.6, 0, 1), bold=True, outline_color=(0, 0, 0, 1), outline_width=2)
        top_layout.add_widget(top_title_label)

        surrender_button = Button(text="Surrender", size_hint=(None, None), size=(150, 50))
        surrender_button.bind(on_press=self.on_surrender_button_pressed)
        top_layout.add_widget(surrender_button)

        self.question_label = Label(text="", font_size=24, color="black")
        top_layout.add_widget(self.question_label)

        self.status_label = Label(text="", font_size=20, color="red")
        top_layout.add_widget(self.status_label)

        ui_hp_all = BoxLayout(orientation='horizontal', spacing=20, padding=(5, 5))
        self.ui_hp_player = Label(text="Your HP: 0", font_size=20, color="black", bold=True)
        self.ui_hp_enemy = Label(text="Enemy HP: 0", font_size=20, color="red", bold=True)
        ui_hp_all.add_widget(self.ui_hp_player)
        ui_hp_all.add_widget(self.ui_hp_enemy)
        top_layout.add_widget(ui_hp_all)

        answer_layout = BoxLayout(orientation='horizontal', spacing=10, padding=(5, 5))
        self.answer_input = TextInput(hint_text="Type your answer here", multiline=False, font_size=18)
        self.answer_input.bind(on_text_validate=self.check_answer)
        submit_button = Button(text="Submit Answer", size_hint=(None, None), size=(150, 50))
        submit_button.bind(on_press=self.check_answer)
        answer_layout.add_widget(self.answer_input)
        answer_layout.add_widget(submit_button)
        top_layout.add_widget(answer_layout)

        self.add_widget(top_layout)
        
        bottom_layout = BoxLayout(orientation='horizontal', spacing=20, padding=(10, 10))
        bottom_layout.size_hint = (None, None)
        bottom_layout.width = self.width  
        bottom_layout.height = self.height * 0.2  
        bottom_layout.center = self.center

        self.add_widget(bottom_layout)

        self.current_hp_enemy = 100
        self.current_hp_player = 100

        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(current_dir, 'bw_data.json')
        with open(data_file_path, 'r') as file:
            data = json.load(file)
        random_index = random.randint(0, len(data['questions']) - 1)
        self.current_question = data['questions'][random_index]['question']
        self.correct_answer = data['questions'][random_index]['answer']
        self.current_question_difficulty = data['questions'][random_index]['difficulty']
        self.update_question()

    def on_surrender_button_pressed(self, instance):
        
        popup = Popup(title='Surrender', size_hint=(None, None), size=(400, 200))

        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        yes_button = Button(text='Yes', size_hint=(None, None), size=(100, 50))
        no_button = Button(text='No', size_hint=(None, None), size=(100, 50))

        yes_button.bind(on_press=lambda instance: self.surrender(popup))
        no_button.bind(on_press=popup.dismiss)

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        content_layout = BoxLayout(orientation='vertical', spacing=10)
        content_layout.add_widget(Label(text='Are you sure you want to surrender?'))
        content_layout.add_widget(button_layout)

        popup.content = content_layout

        popup.open()
    
    def surrender(self, popup_instance):
        popup_instance.dismiss()
        self.construct_main_menu()
        
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

    def attack_enemy(self):
        base_damage = 10
        if self.current_question_difficulty == "easy":
            damage_modifier = 1.0  
        elif self.current_question_difficulty == "medium":
            damage_modifier = 1.5  
        else:  
            damage_modifier = 2.0
        damage = int(random.randint(base_damage, base_damage * 2) * damage_modifier)
        self.current_hp_enemy -= damage
        if self.current_hp_enemy <= 0:  
            self.current_hp_enemy = 0
            self.status_label.text = "Congratulations! You have won the game!"
            self.status_label.color = "lime"
            self.show_end_game_popup()
            return
        self.ui_hp_enemy.text = f"Enemy HP: {self.current_hp_enemy}"

    def enemy_attack(self):
        base_damage = 5
        if self.current_question_difficulty == "easy":
            damage_modifier = 1.0  
        elif self.current_question_difficulty == "medium":
            damage_modifier = 1.5  
        else:  
            damage_modifier = 2.0
        damage = int(random.randint(base_damage, base_damage * 2) * damage_modifier)
        self.current_hp_player -= damage
        if self.current_hp_player <= 0:  
            self.current_hp_player = 0
            self.status_label.text = "Game over! You have been defeated!"
            self.status_label.color = "red"
            self.show_end_game_popup()
            return
        self.ui_hp_player.text = f"Your HP: {self.current_hp_player}"

    def show_end_game_popup(self):
        popup = Popup(title='Game Over', size_hint=(None, None), size=(400, 200))
        content_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content_layout.add_widget(Label(text=self.status_label.text))

        play_again_button = Button(text='Play Again')
        play_again_button.bind(on_press=lambda instance: self.return_to_game(popup))
        content_layout.add_widget(play_again_button)

        button = Button(text='Return to Main Menu')
        button.bind(on_press=lambda instance: self.return_to_main_menu(popup))
        content_layout.add_widget(button)
        
        popup.content = content_layout
        popup.open()

    def return_to_game(self, popup_instance):
        popup_instance.dismiss()
        self.construct_game_menu() 

    def return_to_main_menu(self, popup_instance):
        popup_instance.dismiss()
        self.construct_main_menu() 

    def show_status_clear_text(self, instance):
        self.status_label.text = ""
        
    def focus_answer_input(self, instance):
        self.answer_input.focus = True

    def check_answer(self, instance):
        user_answer = self.answer_input.text.strip().lower()
        if user_answer == self.correct_answer.lower():
            self.status_label.text = "Correct! Next question..."
            self.status_label.color = "lime"
            Clock.schedule_interval(self.show_status_clear_text, 1)
            self.attack_enemy() 
            self.next_question()
        else:
            self.status_label.text = "Wrong! Try again..."
            self.status_label.color = "red"
            Clock.schedule_interval(self.show_status_clear_text, 1)
            self.enemy_attack()  
        Clock.schedule_interval(self.focus_answer_input, 0.1)

class MainApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()
