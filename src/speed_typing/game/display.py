import arcade
from speed_typing.game.controller import controller
from speed_typing.game.constants import RESOURCE_PATH

class Display(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None

    def setup(self):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}TitleScreen.png")
        self.keyboard_sprites = arcade.SpriteList(use_spatial_hash = False)
        self.create_keyboard_sprites()

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
        #self.sprite.draw()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol, True)
