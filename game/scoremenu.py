from arcade import View, load_texture, gui, start_render, draw_lrwh_rectangle_textured, draw_text, color
import game.controller as controller
from game.constants import RESOURCE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH, SFX_DICT, SFX_HANDLER, MUSIC_DICT, MUSIC_HANDLER

class ScoreMenu(View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self, stat_tracker):
        self.background = load_texture(f"{RESOURCE_PATH}backgrounds/Paper.png")

        self.manager = gui.UIManager()
        self.manager.enable()
        self.vBox = gui.UIBoxLayout(vertical = True)

        backButtonTexture = load_texture(f":resources:onscreen_controls/shaded_dark/back.png")  # TODO This needs a custom texture.
        backButton = gui.UITextureButton(texture=backButtonTexture,texture_hovered=backButtonTexture, scale= 1.5)
        
        @backButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 0,)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])
        
        self.vBox.add(backButton.with_space_around(right = 80, left = 80))

        self.manager.add(gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", align_x=660, align_y=-350, child = self.vBox))

        self.manager.add(gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])


    def on_draw(self):
        start_render()
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()
        draw_text(f"Score: 0", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, color.GREEN, 44, 500, "center", "Ultra")  # TODO This needs to receive a score from stattracker.py "Score: 0" is a placeholder.


    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)