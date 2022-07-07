from arcade import load_texture, gui, View, start_render, draw_lrwh_rectangle_textured
import game.controller as controller
from game.constants import RESOURCE_PATH, SFX_DICT, SFX_HANDLER, MUSIC_HANDLER, MUSIC_DICT

class TrainingMenu(View):
    def __init__(self):
        super().__init__()
        # This view has buttons
        self.buttons = True

    def setup(self):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = load_texture(f"{RESOURCE_PATH}Paper.png")

        # manager handles the packing of buttons on the screen
        self.manager = gui.UIManager()
        self.manager.enable()
        self.vBox = gui.UIBoxLayout(vertical = True)

        # Textures for buttons
        topRowTexture = load_texture(f"{RESOURCE_PATH}toprow.png")
        topRowTextureHovered = load_texture(f"{RESOURCE_PATH}toprow_hovered.png")
        middleRowTexture = load_texture(f"{RESOURCE_PATH}middlerow.png")
        middleRowTextureHovered = load_texture(f"{RESOURCE_PATH}middlerow_hovered.png")
        bottomRowTexture = load_texture(f"{RESOURCE_PATH}bottomrow.png")
        bottomRowTextureHovered = load_texture(f"{RESOURCE_PATH}bottomrow_hovered.png")
        allRowTexture = load_texture(f"{RESOURCE_PATH}allrows.png")
        allRowTextureHovered = load_texture(f"{RESOURCE_PATH}allrows_hovered.png")

        # Create the buttons here        
        topButton = gui.UITextureButton(texture = topRowTexture, texture_hovered = topRowTextureHovered, scale = 2)
        middleButton = gui.UITextureButton(texture = middleRowTexture, texture_hovered = middleRowTextureHovered, scale = 2)
        bottomButton = gui.UITextureButton(texture = bottomRowTexture, texture_hovered = bottomRowTextureHovered, scale = 2)
        allButton = gui.UITextureButton(texture = allRowTexture, texture_hovered = allRowTextureHovered, scale = 2)

        # handle waht happens when the user presses the buttons
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

        # Add the buttons to the manager        
        self.vBox.add(topButton.with_space_around(right = 80, left = 70))
        self.vBox.add(middleButton.with_space_around(right = 80, left = 80))
        self.vBox.add(bottomButton.with_space_around(right = 80, left = 80))
        self.vBox.add(allButton.with_space_around(right = 80, left = 80))

        # pack the manager to the screen
        self.manager.add(gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", child = self.vBox))

        self.manager.add(gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        # start playing music for the screen
        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])

    def on_draw(self):
        start_render()
        # draws the background
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        """
        Stops buttons from being active while view is not visible
        """
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        # handle key presses for exit and back
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)