import arcade
import arcade.gui
import game.constants as const
import game.controller as controller
from game.constants import RESOURCE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH

class InstructionsMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}Paper.png")

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.vBox = arcade.gui.UIBoxLayout(vertical = True)

        backButtonTexture = arcade.load_texture(f":resources:onscreen_controls/shaded_dark/back.png")  # TODO This needs a custom texture.
        backButton = arcade.gui.UITextureButton(texture=backButtonTexture,texture_hovered=backButtonTexture, scale= 1.5)
        
        @backButton.event("on_click")
        def on_click_texture_button(event):
            controller.Controller.on_change_view(self, 0, difficulty = "TOP")
            const.SFX_HANDLER.play_sfx(const.SFX_DICT["whoosh"])
        
        self.vBox.add(backButton.with_space_around(right = 80, left = 80))

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", align_x=660, align_y=-350, child = self.vBox))

        self.manager.add(arcade.gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        const.MUSIC_HANDLER.play_song(const.MUSIC_DICT["wind"])


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()
        arcade.draw_text(f"This is a placeholder for the instructions menu.", SCREEN_WIDTH / 2, SCREEN_HEIGHT, arcade.color.BLACK, 44, 500, "center", "Ultra")  # TODO Create actual instructions.

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.Controller.get_key_press(self, symbol = symbol, modifier = modifiers)