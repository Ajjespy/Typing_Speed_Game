import arcade
import game.controller
from game.constants import RESOURCE_PATH, FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from game.random_word import RandomWord
from time import time
from random import randint

class LevelGenerator(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None

class Typing(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None
        
    def setup(self, difficulty = "ALL"):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = arcade.load_texture(f"{RESOURCE_PATH}ShootZone.png")
        self.keyboard_sprites = arcade.SpriteList(use_spatial_hash = False)
        self.create_keyboard_sprites()
        if difficulty == "ALL":
            if randint(0, 1) == 1:
                self.randomWord = RandomWord.get_random_chars(length = 12, row = difficulty)
            else:
                self.randomWord = RandomWord.get_word(randint(1, 8))
        else:
            self.randomWord = RandomWord.get_random_chars(length = 12, row = difficulty)
        self.userType = ""
        self.last_time = 0
        self.num_words = 0
        self.start_type_time = None
        self.end_type_time = None
        self.difficulty = difficulty


    def on_draw(self):
        # background gets drawn first
        super().on_draw()
        arcade.start_render()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # checks if the user has typed in the correct word
        if len(self.userType) > len(self.randomWord) - 1 and self.userType == self.randomWord:
            # stat checker stuff
            self.end_type_time = time()
            self.last_time = self.end_type_time - self.start_type_time

            if self.difficulty == "ALL":
                if randint(0, 1) == 1:
                    self.randomWord = RandomWord.get_random_chars(length = 12, row = self.difficulty)
                else:
                    self.randomWord = RandomWord.get_word(randint(1, 8))
            else:
                self.randomWord = RandomWord.get_random_chars(length = 12, row = self.difficulty)

            self.num_words += 1
            self.userType = ""

        elif len(self.userType) > len(self.randomWord) - 1:
            self.userType = ""

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None

    def on_key_press(self, symbol: int, modifiers: int):
        game.controller.Controller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            # basic stat checker will be finished in stat checker file
            if self.end_type_time == None and self.start_type_time == None:
                self.start_type_time = time()
            
            # checks for upper case chars
            if modifiers % 2 == 1:
                self.userType = self.userType + chr(symbol).upper()
            else:
                self.userType = self.userType + chr(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        # lets controller know that a key has become unpressed
        game.controller.Controller.get_key_press(self, symbol, True)