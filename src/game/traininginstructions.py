import arcade
import arcade.gui
import game.controller as controller
from game.constants import SFX_DICT, SFX_HANDLER, MUSIC_DICT, MUSIC_HANDLER, RESOURCE_PATH

class TrainingInstructions(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self, difficulty = "TOP"):
        self.background = arcade.load_texture(f"{RESOURCE_PATH}Paper.png")
        self.difficulty = difficulty

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.vBox = arcade.gui.UIBoxLayout(vertical = True)

        nextTexture = arcade.load_texture(f"{RESOURCE_PATH}keys_unpressed/Mark_Right_Key_dark.png")
        nextTextureHovered = arcade.load_texture(f"{RESOURCE_PATH}keys_pressed/Mark_Right_Key_Light.png")
        
        nextButton = arcade.gui.UITextureButton(texture = nextTexture, texture_hovered = nextTextureHovered, scale = 1)

        @nextButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 6, difficulty = self.difficulty)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        self.vBox.add(nextButton.with_space_around(right = 80, left = 80))

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x = "right", anchor_y = "bottom", align_x = -50, align_y = 50, child = self.vBox))

        self.manager.add(arcade.gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        arcade.draw_text("""Howdy, and welcome to the training section of the game.
        Typing is a very handy skill to have.
        Lets learn some basics.
        
        In order to type quickly you have to use the correct technique. 
        Find the 'F' and 'J' keys on your keyboard. Place your index finger of your left hand on 'F' and the index finger of your right hand on 'J'.
        The middle row of the keyboard is called the Home Row and is where your hands should always start when you type.
        
        Now that you know where to place your hands lets start typing!
        (Click the Next Button Below)""", 100, self.window.height - 100, color = arcade.color.BLACK, font_size= 24, width = self.window.width - 200, align = "center", font_name = "Ultra")
        
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)