import arcade
<<<<<<< HEAD:src/speed_typing/game/training.py
import speed_typing.game.controller as controller
from speed_typing.game.constants import RESOURCE_PATH, FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from speed_typing.game.random_word import RandomWord
=======
import game.controller
from game.constants import RESOURCE_PATH, FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from game.random_word import RandomWord
from time import time
>>>>>>> main:game/training.py

class Training(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None
        
    def setup(self):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = arcade.load_texture(f"{RESOURCE_PATH}Paper.png")
        self.keyboard_sprites = arcade.SpriteList(use_spatial_hash = False)
        self.create_keyboard_sprites()
        self.randomWord = RandomWord.get_random_chars(length = 12)
        self.userType = ""
        self.last_time = 0
        self.num_words = 1
        self.start_type_time = None
        self.end_type_time = None

    def create_keyboard_sprites(self):
        """
        Creates the sprites for the on screen keyboard. Should be run in the setup function.
        """
        # Code to display the numbers for the onscreen keyboard currently not in use so commented out
        # for i in range(1, 11):
        #     new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/{i % 10}_Key_Dark.png", 1)
        #     new_sprite.center_x = self.window.width / 4 + (i-1) * 72
        #     new_sprite.center_y = self.window.height / 2
        #     self.keyboard_sprites.append(new_sprite)
        #     del new_sprite

        letters_keyboard_order = "QWERTYUIOPASDFGHJKLZXCVBNM"
        i = 0

        #Creates the sprites or A-Z and positions them on screen
        for letter in letters_keyboard_order:
            new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/{letter}_Key_Dark.png", 1)
            if i < 10:
                new_sprite.center_x = self.window.width / 4 + i * 72 + 36
                new_sprite.center_y = self.window.height / 2 - 72 * 2
            elif i < 19:
                new_sprite.center_x = self.window.width / 4 + (i - 10) * 72 + 36 + 18 + 12
                new_sprite.center_y = self.window.height / 2 - 72 * 3
            elif i < 27:
                new_sprite.center_x = self.window.width / 4 + (i - 19) * 72 + 90 + 48
                new_sprite.center_y = self.window.height / 2 - 72 * 4
            self.keyboard_sprites.append(new_sprite)
            del new_sprite
            i += 1
        #Shift Sprite
        new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png", 1.46)
        new_sprite.center_x = self.window.width / 4 - 17 + 48
        new_sprite.center_y = self.window.height / 2 - 72 * 4
        self.keyboard_sprites.append(new_sprite)
        del new_sprite


    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        # background gets drawn first
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.keyboard_sprites.draw()
        arcade.draw_text(self.randomWord, self.window.width/4, self.window.height * 3/4 - 48, arcade.color.RED, 44, 400, "left", font_name="Ultra")
        arcade.draw_text(self.userType, self.window.width/4, self.window.height * 3/4 - 200, arcade.color.BLUE, 44, 400, "left", font_name="Ultra")
        arcade.draw_text(f"Sec: {int((self.last_time))}", self.window.width - 400, self.window.height - 48, arcade.color.GREEN, 44, 500, "center", "Ultra")  
        arcade.draw_text(f"Words: {self.num_words}", self.window.width - 450, self.window.height - 100, arcade.color.GREEN, 44, 500, "center", "Ultra")

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # checks if the user has typed in the correct word
        if len(self.userType) > 11 and self.userType == self.randomWord:
            # stat checker stuff
            self.end_type_time = time()
            self.last_time = self.end_type_time - self.start_type_time
            self.randomWord = RandomWord.get_random_chars(12)
            self.num_words += 1
            self.userType = ""

        elif len(self.userType) > 11:
            self.userType = ""

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None

    def on_key_press(self, symbol: int, modifiers: int):
        controller.Controller.get_key_press(self, symbol)
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
<<<<<<< HEAD:src/speed_typing/game/training.py
        controller.Controller.get_key_press(self, symbol, True)
=======
        # lets controller know that a key has become unpressed
        game.controller.Controller.get_key_press(self, symbol, True)
>>>>>>> main:game/training.py

    def on_resize(self, width: int, height: int):
        """
        Currently no way to resize but necessary if we add in the future
        """
        if(width <= SCREEN_WIDTH):
            for i in range(len(self.keyboard_sprites)-1):
                self.keyboard_sprites[i].scale = 0.5
                if i < 10:
                    self.keyboard_sprites[i].center_x = width / 4 + (i+1) * 72/2
                    self.keyboard_sprites[i].center_y = height / 2
                elif i < 20:
                    self.keyboard_sprites[i].center_x = width / 4 + (i-10) * 72/2 + 36
                    self.keyboard_sprites[i].center_y = height / 2 - 72/2
                elif i < 29:
                    self.keyboard_sprites[i].center_x = width / 4 + (i - 20) * 72/2 + 36 + 18
                    self.keyboard_sprites[i].center_y = height / 2 - 72/2 * 2
                elif i < 37:
                    self.keyboard_sprites[i].center_x = width / 4 + (i - 29) * 72/2 + 90
                    self.keyboard_sprites[i].center_y = height / 2 - 72/2 * 3
            
            self.keyboard_sprites[len(self.keyboard_sprites)-1].scale = 1.42/2
            self.keyboard_sprites[len(self.keyboard_sprites)-1].center_x = self.window.width / 4 + 36
            self.keyboard_sprites[len(self.keyboard_sprites)-1].center_y = self.window.height / 2 - 72/2 * 3
        else:
            for i in range(len(self.keyboard_sprites)-1):
                self.keyboard_sprites[i].scale = 1
                if i < 10 :
                    self.keyboard_sprites[i].center_x = self.window.width / 4 + (i) * 72
                    self.keyboard_sprites[i].center_y = self.window.height / 2
                elif i < 20:
                    self.keyboard_sprites[i].center_x = self.window.width / 4 + (i -10) * 72 + 36
                    self.keyboard_sprites[i].center_y = self.window.height / 2 - 72
                elif i < 29:
                    self.keyboard_sprites[i].center_x = self.window.width / 4 + (i - 20) * 72 + 36 + 18
                    self.keyboard_sprites[i].center_y = self.window.height / 2 - 72 * 2
                elif i < 37:
                    self.keyboard_sprites[i].center_x = self.window.width / 4 + (i - 29) * 72 + 90
                    self.keyboard_sprites[i].center_y = self.window.height / 2 - 72 * 3
            
            self.keyboard_sprites[len(self.keyboard_sprites)-1].scale = 1.42
            self.keyboard_sprites[len(self.keyboard_sprites)-1].center_x = self.window.width / 4 - 17
            self.keyboard_sprites[len(self.keyboard_sprites)-1].center_y = self.window.height / 2 - 72 * 3