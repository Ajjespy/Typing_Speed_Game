from arcade import load_texture, SpriteList, Sprite, View, start_render, draw_text, draw_lrwh_rectangle_textured, key, color
import game.controller as controller
from game.constants import RESOURCE_PATH, MUSIC_HANDLER, MUSIC_DICT, SFX_DICT, SFX_HANDLER
from game.random_word import RandomWord
from time import time
from random import randint
import game.stattracker as stat

class Training(View):
    def __init__(self):
        super().__init__()
        # Has no buttons
        self.buttons = False
        
    def setup(self, difficulty = "ALL"):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        # user has to type 20 words to pass this level of training
        self.words_left = 20

        # stat tracker object used to store WPM and other useful information
        self.stattracker = stat.StatTracker()

        self.background = load_texture(f"{RESOURCE_PATH}backgrounds/Paper.png")

        # onscreen keyboard spritelist
        self.keyboard_sprites = SpriteList(use_spatial_hash = False)

        self.create_keyboard_sprites()

        # generates random word depending on the difficulty
        if difficulty == "ALL":
            if randint(0, 1) == 1:
                self.randomWord = RandomWord.get_random_chars(length = randint(4, 8), row = difficulty)
                self.stattracker.add_word(self.randomWord)
            else:
                # 70% chance of it being an easy word 20% a harder word 10% very difficult word
                prob = randint(1,10)
                if prob in [1,2,3,4,5,6,7]:
                    self.randomWord = RandomWord.get_word(randint(1, 3))
                elif prob in [8,9]:
                    self.randomWord = RandomWord.get_word(randint(4, 5))
                else:
                    self.randomWord = RandomWord.get_word(randint(6, 8))
                    
                self.stattracker.add_word(self.randomWord)
        else:
            self.randomWord = RandomWord.get_random_chars(length = randint(4, 8), row = difficulty)
            self.stattracker.add_word(self.randomWord)

        
        self.userType = ""
        self.last_time = 0
        self.num_words = 0
        self.start_type_time = None
        self.end_type_time = None
        self.difficulty = difficulty

        # sound
        MUSIC_HANDLER.play_song(MUSIC_DICT["saloon_honkey_tonk"], .15)

    def create_keyboard_sprites(self):
        """
        Creates the sprites for the on screen keyboard. Should be run in the setup function. All sprites are stored in SpriteList.
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

        #Creates the sprites for A-Z and positions them on screen
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

        # draws the on screen keyboard
        self.keyboard_sprites.draw()

        # draws what the user is typing and what the user needs to type
        draw_text(self.randomWord, self.window.width / 2 - 44 * 5.5, self.window.height * 3 / 4 - 48, color.RED, 44, 400, "left", font_name="Ultra")
        draw_text(self.userType, self.window.width / 2 - 44 * 5.5, self.window.height * 3 / 4 - 200, color.BLUE, 44, 400, "left", font_name="Ultra")
        # simple stat tracker for instant stats
        draw_text(f"Sec: {int(self.last_time)}", self.window.width - 400, self.window.height - 48, color.GREEN, 44, 500, "center", "Ultra")  
        draw_text(f"Words: {self.num_words}", self.window.width - 450, self.window.height - 100, color.GREEN, 44, 500, "center", "Ultra")

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # clears what the user has typed after they reach the length of the word does not check accuracy
        if len(self.userType) > len(self.randomWord) - 1:
            # stat checker stuff
            self.end_type_time = time()
            self.last_time = self.end_type_time - self.start_type_time
            self.words_left -= 1
            # plays sound when word is typed correctly
            SFX_HANDLER.play_sfx(SFX_DICT["ding"], 1.5)

            # generates new random word for user to type
            if self.difficulty == "ALL":
                if randint(0, 1) == 1:
                    self.randomWord = RandomWord.get_random_chars(length = randint(4, 8), row = self.difficulty)
                    if self.words_left != 0:
                        self.stattracker.add_word(self.randomWord)
                else:
                    # 70% chance of it being an easy word 20% a harder word 10% very difficult word
                    prob = randint(1,10)
                    if prob in [1,2,3,4,5,6,7]:
                        self.randomWord = RandomWord.get_word(randint(1, 3))
                    elif prob in [8,9]:
                        self.randomWord = RandomWord.get_word(randint(4, 5))
                    else:
                        self.randomWord = RandomWord.get_word(randint(6, 8))

                    if self.words_left != 0:
                        self.stattracker.add_word(self.randomWord)
            else:
                self.randomWord = RandomWord.get_random_chars(length = randint(4, 8), row = self.difficulty)
                if self.words_left != 0:
                    self.stattracker.add_word(self.randomWord)

            # resets the user input so they can type a new word
            self.num_words += 1
            self.stattracker.add_user_word(self.userType)
            self.userType = ""

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None

        if self.words_left <= 0:
            # after user has typed all 20 words go to the stat screen for stattracker information
            self.stattracker.set_end()
            controller.on_change_view(self, 3, stat_tracker = self.stattracker)

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            if self.stattracker.start_time == 0:
                self.stattracker.set_start()
            # basic stat checker will be finished in stat checker file
            if self.end_type_time == None and self.start_type_time == None:
                self.start_type_time = time()
            
            # checks for upper case chars
            if modifiers % 2 == 1:
                self.userType = self.userType + chr(symbol).upper()
            else:
                self.userType = self.userType + chr(symbol)
        # user can backspace characters as long as they have not reached the end of the word
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