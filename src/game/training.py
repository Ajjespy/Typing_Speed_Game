from arcade import load_texture, SpriteList, Sprite, View, start_render, draw_text, draw_lrwh_rectangle_textured, key, color
import game.controller as controller
from game.constants import RESOURCE_PATH, SCREEN_WIDTH, MUSIC_HANDLER, MUSIC_DICT, SFX_DICT, SFX_HANDLER
from game.random_word import RandomWord
from time import time
from random import randint
import game.stattracker as stat

class Training(View):
    def __init__(self):
        super().__init__()
        self.background = None
        self.buttons = False
        
    def setup(self, difficulty = "ALL"):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.words_left = 20
        self.stattracker = stat.StatTracker()
        self.background = load_texture(f"{RESOURCE_PATH}Paper.png")
        self.keyboard_sprites = SpriteList(use_spatial_hash = False)
        self.create_keyboard_sprites()
        if difficulty == "ALL":
            if randint(0, 1) == 1:
                self.randomWord = RandomWord.get_random_chars(length = randint(4, 10), row = difficulty)
            else:
                self.randomWord = RandomWord.get_word(randint(1, 8))
        else:
            self.randomWord = RandomWord.get_random_chars(length = randint(4, 10), row = difficulty)
        self.userType = ""
        self.last_time = 0
        self.num_words = 0
        self.start_type_time = None
        self.end_type_time = None
        self.difficulty = difficulty

        MUSIC_HANDLER.play_song(MUSIC_DICT["saloon_honkey_tonk"])

    def create_keyboard_sprites(self):
        """
        Creates the sprites for the on screen keyboard. Should be run in the setup function.
        """
        # Code to display the numbers for the onscreen keyboard currently not in use so commented out
        # for i in range(1, 11):
        #     new_sprite = Sprite(f"{RESOURCE_PATH}keys_unpressed/{i % 10}_Key_Dark.png", 1)
        #     new_sprite.center_x = self.window.width / 4 + (i-1) * 72
        #     new_sprite.center_y = self.window.height / 2
        #     self.keyboard_sprites.append(new_sprite)
        #     del new_sprite

        letters_keyboard_order = "QWERTYUIOPASDFGHJKLZXCVBNM"
        i = 0

        #Creates the sprites or A-Z and positions them on screen
        for letter in letters_keyboard_order:
            new_sprite = Sprite(f"{RESOURCE_PATH}keys_unpressed/{letter}_Key_Dark.png", 1)
            if i < 5:
                new_sprite.center_x = self.window.width / 2 - abs(i - 4) * 72
                new_sprite.center_y = self.window.height / 2 - 72 * 2
            elif i < 10:
                new_sprite.center_x = self.window.width / 2 + abs(i - 4) * 72
                new_sprite.center_y = self.window.height / 2 - 72 * 2
            elif i < 14:
                new_sprite.center_x = self.window.width / 2 - abs(i - 13) * 72 - 36
                new_sprite.center_y = self.window.height / 2 - 72 * 3
            elif i < 19:
                new_sprite.center_x = self.window.width / 2 + abs(i - 13) * 72 - 36
                new_sprite.center_y = self.window.height / 2 - 72 * 3
            elif i < 22:
                new_sprite.center_x = self.window.width / 2 - abs(i - 21) * 72 - 36
                new_sprite.center_y = self.window.height / 2 - 72 * 4
            elif i < 27:
                new_sprite.center_x = self.window.width / 2 + abs(i - 21) * 72 - 36
                new_sprite.center_y = self.window.height / 2 - 72 * 4
            self.keyboard_sprites.append(new_sprite)
            del new_sprite
            i += 1
        #Shift Sprite
        new_sprite = Sprite(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png", 1.46)
        new_sprite.center_x = self.window.width / 2 - 4 * 72
        new_sprite.center_y = self.window.height / 2 - 72 * 4
        self.keyboard_sprites.append(new_sprite)
        del new_sprite


    def on_draw(self):
        super().on_draw()
        start_render()
        # background gets drawn first
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.keyboard_sprites.draw()
        draw_text(self.randomWord, self.window.width / 2 - 44 * 5.5, self.window.height * 3 / 4 - 48, color.RED, 44, 400, "left", font_name="Ultra")
        draw_text(self.userType, self.window.width / 2 - 44 * 5.5, self.window.height * 3 / 4 - 200, color.BLUE, 44, 400, "left", font_name="Ultra")
        draw_text(f"Sec: {int(self.last_time)}", self.window.width - 400, self.window.height - 48, color.GREEN, 44, 500, "center", "Ultra")  
        draw_text(f"Words: {self.num_words}", self.window.width - 450, self.window.height - 100, color.GREEN, 44, 500, "center", "Ultra")

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # checks if the user has typed in the correct word
        if len(self.userType) > len(self.randomWord) - 1 and self.userType == self.randomWord:
            # stat checker stuff
            self.end_type_time = time()
            self.last_time = self.end_type_time - self.start_type_time
            self.words_left -= 1
            SFX_HANDLER.play_sfx(SFX_DICT["ding"], 1.5)

            if self.difficulty == "ALL":
                if randint(0, 1) == 1:
                    self.randomWord = RandomWord.get_random_chars(length = randint(4, 10), row = self.difficulty)
                else:
                    self.randomWord = RandomWord.get_word(randint(1, 8))
            else:
                self.randomWord = RandomWord.get_random_chars(length = randint(4, 10), row = self.difficulty)

            self.num_words += 1
            self.userType = ""

        elif len(self.userType) > len(self.randomWord) - 1:
            self.userType = ""

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None

        if self.words_left <= 0:
            controller.on_change_view(self, 3, self.stattracker)

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            # basic stat checker will be finished in stat checker file
            if self.end_type_time == None and self.start_type_time == None:
                self.start_type_time = time()
            
            # checks for upper case chars
            if modifiers % 2 == 1:
                self.userType = self.userType + chr(symbol).upper()
            else:
                self.userType = self.userType + chr(symbol)
        if symbol == key.BACKSPACE:
            self.userType = self.userType[:-1]

    def on_key_release(self, symbol: int, modifiers: int):
        # lets controller know that a key has become unpressed
        controller.get_key_press(self, symbol, True)

    def on_resize(self, width: int, height: int):
        """
        Currently no way to resize but necessary if we add in the future
        """
        super().on_resize(width, height)