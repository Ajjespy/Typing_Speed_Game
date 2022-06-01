import arcade
from game.trainingcontroller import trainingcontroller
from game.constants import RESOURCE_PATH, FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from game.random_word import RandomWord

class Training(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None

    def setup(self):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}Paper.png")
        self.keyboard_sprites = arcade.SpriteList(use_spatial_hash = False)
        self.create_keyboard_sprites()
        self.randomWord = RandomWord.get_random_chars(length = 12)
        self.userType = ""

    def create_keyboard_sprites(self):
        for i in range(1, 11):
            new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/{i % 10}_Key_Dark.png", 1)
            new_sprite.center_x = self.window.width / 4 + (i-1) * 72
            new_sprite.center_y = self.window.height / 2
            self.keyboard_sprites.append(new_sprite)
            del new_sprite

        letters_keyboard_order = "QWERTYUIOPASDFGHJKLZXCVBNM"
        i = 0

        for letter in letters_keyboard_order:
            new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/{letter}_Key_Dark.png", 1)
            if i < 10:
                new_sprite.center_x = self.window.width / 4 + i * 72 + 36
                new_sprite.center_y = self.window.height / 2 - 72
            elif i < 19:
                new_sprite.center_x = self.window.width / 4 + (i - 10) * 72 + 36 + 18
                new_sprite.center_y = self.window.height / 2 - 72 * 2
            elif i < 27:
                new_sprite.center_x = self.window.width / 4 + (i - 19) * 72 + 90
                new_sprite.center_y = self.window.height / 2 - 72 * 3
            self.keyboard_sprites.append(new_sprite)
            del new_sprite
            i += 1

        new_sprite = arcade.Sprite(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png", 1.42)
        new_sprite.center_x = self.window.width / 4 - 17
        new_sprite.center_y = self.window.height / 2 - 72 * 3
        self.keyboard_sprites.append(new_sprite)
        del new_sprite


    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.keyboard_sprites.draw()
        arcade.draw_text(self.randomWord, self.window.width/4, self.window.height*3/4, arcade.color.RED, 44, 400, "left", font_name="Ultra")
        arcade.draw_text(self.userType, self.window.width/4, self.window.height*3/4 - 100, arcade.color.BLUE, 44, 400, "left", font_name="Ultra")

    def on_update(self, delta_time: float):
        super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        trainingcontroller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            if len(self.userType) > 12:
                self.userType = ""
            self.userType = self.userType + chr(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        trainingcontroller.get_key_press(self, symbol, True)

    def on_resize(self, width: int, height: int):
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
            
