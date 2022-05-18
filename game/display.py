import arcade
from game.controller import controller
from game.constants import RESOURCE_PATH

class Display(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None

    def setup(self):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}TitleScreen.png")

    def on_draw(self):
        super().on_draw()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)

    def on_update(self, delta_time: float):
        super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self,symbol)