from arcade import load_texture, gui, View, start_render, draw_lrwh_rectangle_textured
import game.controller as controller
from game.constants import RESOURCE_PATH, SFX_DICT, SFX_HANDLER, MUSIC_HANDLER, MUSIC_DICT

class TrainingMenu(View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self):
        self.background = load_texture(f"{RESOURCE_PATH}Paper.png")

        self.manager = gui.UIManager()
        self.manager.enable()
        self.vBox = gui.UIBoxLayout(vertical = True)

        topRowTexture = load_texture(f"{RESOURCE_PATH}toprow.png")
        topRowTextureHovered = load_texture(f"{RESOURCE_PATH}toprow_hovered.png")
        middleRowTexture = load_texture(f"{RESOURCE_PATH}middlerow.png")
        middleRowTextureHovered = load_texture(f"{RESOURCE_PATH}middlerow_hovered.png")
        bottomRowTexture = load_texture(f"{RESOURCE_PATH}bottomrow.png")
        bottomRowTextureHovered = load_texture(f"{RESOURCE_PATH}bottomrow_hovered.png")
        allRowTexture = load_texture(f"{RESOURCE_PATH}allrows.png")
        allRowTextureHovered = load_texture(f"{RESOURCE_PATH}allrows_hovered.png")
        
        topButton = gui.UITextureButton(texture = topRowTexture, texture_hovered = topRowTextureHovered, scale = 2)
        middleButton = gui.UITextureButton(texture = middleRowTexture, texture_hovered = middleRowTextureHovered, scale = 2)
        bottomButton = gui.UITextureButton(texture = bottomRowTexture, texture_hovered = bottomRowTextureHovered, scale = 2)
        allButton = gui.UITextureButton(texture = allRowTexture, texture_hovered = allRowTextureHovered, scale = 2)

        @topButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 2, difficulty = "TOP")
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @middleButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 2, difficulty = "MIDDLE")
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @bottomButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 2, difficulty = "BOTTOM")
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @allButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 2, difficulty = "ALL")
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])
        
        self.vBox.add(topButton.with_space_around(right = 80, left = 70))
        self.vBox.add(middleButton.with_space_around(right = 80, left = 80))
        self.vBox.add(bottomButton.with_space_around(right = 80, left = 80))
        self.vBox.add(allButton.with_space_around(right = 80, left = 80))

        self.manager.add(gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", child = self.vBox))

        self.manager.add(gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])

    def on_draw(self):
        start_render()
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)