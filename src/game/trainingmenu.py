import arcade
import game.controller as controller
from game.constants import *
import game.constants as const

class TrainingMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}Paper.png")

        MUSIC_HANDLER.update_music_list([f"{const.RESOURCE_PATH}/music/a-gentle-breeze-wind-4-14681.mp3",])  # add music here
        MUSIC_HANDLER.play_song()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.vBox = arcade.gui.UIBoxLayout(vertical = True)

        topRowTexture = arcade.load_texture(f"{RESOURCE_PATH}toprow.png")
        topRowTextureHovered = arcade.load_texture(f"{RESOURCE_PATH}toprow_hovered.png")
        middleRowTexture = arcade.load_texture(f"{RESOURCE_PATH}middlerow.png")
        middleRowTextureHovered = arcade.load_texture(f"{RESOURCE_PATH}middlerow_hovered.png")
        bottomRowTexture = arcade.load_texture(f"{RESOURCE_PATH}bottomrow.png")
        bottomRowTextureHovered = arcade.load_texture(f"{RESOURCE_PATH}bottomrow_hovered.png")
        allRowTexture = arcade.load_texture(f"{RESOURCE_PATH}allrows.png")
        allRowTextureHovered = arcade.load_texture(f"{RESOURCE_PATH}allrows_hovered.png")
        
        topButton = arcade.gui.UITextureButton(texture = topRowTexture, texture_hovered = topRowTextureHovered, scale = 2)
        middleButton = arcade.gui.UITextureButton(texture = middleRowTexture, texture_hovered = middleRowTextureHovered, scale = 2)
        bottomButton = arcade.gui.UITextureButton(texture = bottomRowTexture, texture_hovered = bottomRowTextureHovered, scale = 2)
        allButton = arcade.gui.UITextureButton(texture = allRowTexture, texture_hovered = allRowTextureHovered, scale = 2)

        @topButton.event("on_click")
        def on_click_texture_button(event):
            controller.Controller.on_change_view(self, 2, difficulty = "TOP")

        @middleButton.event("on_click")
        def on_click_texture_button(event):
            controller.Controller.on_change_view(self, 2, difficulty = "MIDDLE")

        @bottomButton.event("on_click")
        def on_click_texture_button(event):
            controller.Controller.on_change_view(self, 2, difficulty = "BOTTOM")

        @allButton.event("on_click")
        def on_click_texture_button(event):
            controller.Controller.on_change_view(self, 2, difficulty = "ALL")
        
        self.vBox.add(topButton.with_space_around(right = 80, left = 70))
        self.vBox.add(middleButton.with_space_around(right = 80, left = 80))
        self.vBox.add(bottomButton.with_space_around(right = 80, left = 80))
        self.vBox.add(allButton.with_space_around(right = 80, left = 80))

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", child = self.vBox))

        self.manager.add(arcade.gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        MUSIC_HANDLER.update_music_list([f"{const.RESOURCE_PATH}/music/a-gentle-breeze-wind-4-14681.mp3",])  # add music here
        MUSIC_HANDLER.play_song()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.Controller.get_key_press(self, symbol = symbol, modifier = modifiers)