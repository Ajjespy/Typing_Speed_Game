from arcade import gui, View, load_texture, draw_text, start_render, color, draw_lrwh_rectangle_textured
import game.controller as controller
from game.constants import SFX_DICT, SFX_HANDLER, MUSIC_DICT, MUSIC_HANDLER, RESOURCE_PATH

class TrainingInstructions(View):
    def __init__(self):
        super().__init__()
        # this view has buttons
        self.buttons = True

    def setup(self):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = load_texture(f"{RESOURCE_PATH}backgrounds/Paper.png")

        # manager handles buttons
        self.manager = gui.UIManager()
        self.manager.enable()
        self.vBox = gui.UIBoxLayout(vertical = True)

        # textures for buttons
        nextTexture = load_texture(f"{RESOURCE_PATH}keys_unpressed/Mark_Right_Key_dark.png")
        nextTextureHovered = load_texture(f"{RESOURCE_PATH}keys_pressed/Mark_Right_Key_Light.png")
        
        nextButton = gui.UITextureButton(texture = nextTexture, texture_hovered = nextTextureHovered, scale = 1)

        # action the button takes when clicked
        @nextButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 6)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        # pack button to screen
        self.vBox.add(nextButton.with_space_around(right = 80, left = 80))

        self.manager.add(gui.UIAnchorWidget(anchor_x = "right", anchor_y = "bottom", align_x = -50, align_y = 50, child = self.vBox))

        self.manager.add(gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        # sound
        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])

    def on_draw(self):
        start_render()
        # Draws background first
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        draw_text("""Howdy, and welcome to the training section of the game.
        Typing is a very handy skill to have.
        Lets learn some basics.
        
        In order to type quickly you have to use the correct technique. 
        Find the 'F' and 'J' keys on your keyboard. Place your index finger of your left hand on 'F' and the index finger of your right hand on 'J'.
        The middle row of the keyboard is called the Home Row and is where your hands should always start when you type.
        
        Now that you know where to place your hands lets start typing!
        (Click the Next Button Below)""", 100, self.window.height - 100, color = color.BLACK, font_size= 24, width = self.window.width - 200, align = "center", font_name = "Ultra")
        # draws buttons
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        """
        Stops buttons from being active while view is not visible
        """
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        # handle keypresses for back and exit
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)