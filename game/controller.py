import arcade
from arcade.key import F

class controller:
    def get_key_press(director, symbol):
        if symbol == F:
            director.window.set_fullscreen(not director.window.fullscreen)