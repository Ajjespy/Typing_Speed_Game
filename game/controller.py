import arcade
from game.constants import RESOURCE_PATH, convertLetters

class controller:
    def get_key_press(director, symbol, unpress = False):
        
        if symbol == arcade.key.ESCAPE and not unpress:
            director.window.set_fullscreen(not director.window.fullscreen)

        if symbol in set(range(97,123)) and not unpress:
            try:
                director.keyboard_sprites[convertLetters[chr(symbol).upper()] + 9].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_pressed/{chr(symbol -97 + 65)}_Key_Light.png")
            except:
                pass

        if symbol in set(range(97,123)) and unpress:
            try:
                director.keyboard_sprites[convertLetters[chr(symbol).upper()] + 9].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_unpressed/{chr(symbol -97 + 65)}_Key_Dark.png")
            except:
                pass

        if (symbol == arcade.key.LSHIFT or symbol == arcade.key.RSHIFT) and not unpress:
            director.keyboard_sprites[len(director.keyboard_sprites)-1].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_pressed/Shift_Alt_Key_Light.png")

        if (symbol == arcade.key.LSHIFT or symbol == arcade.key.RSHIFT) and unpress:
            director.keyboard_sprites[len(director.keyboard_sprites)-1].texture = arcade.load_texture(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png")