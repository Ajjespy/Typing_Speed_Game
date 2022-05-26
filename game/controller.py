import arcade
from arcade.key import ESCAPE
from game.constants import RESOURCE_PATH

class controller:
    def get_key_press(director, symbol, unpress = False):
        if symbol == arcade.key.ESCAPE and not unpress:
            director.window.set_fullscreen(not director.window.fullscreen)

        if symbol in set(range(97,123)) and not unpress:
            director.keyboard_sprites[symbol - 97 + 10].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_pressed/{chr(symbol -97 + 65)}_Key_Light.png")
            pass

        if symbol in set(range(97,123)) and unpress:
            director.keyboard_sprites[symbol - 97 + 10].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_unpressed/{chr(symbol -97 + 65)}_Key_Dark.png")

