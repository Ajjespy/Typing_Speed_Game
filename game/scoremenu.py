from arcade import View, load_texture, gui, start_render, draw_lrwh_rectangle_textured, draw_text, color
import game.controller as controller
from game.constants import RESOURCE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH, SFX_DICT, SFX_HANDLER, MUSIC_DICT, MUSIC_HANDLER

class ScoreMenu(View):
    def __init__(self):
        super().__init__()
        self.buttons = True

    def setup(self, stat_tracker):
        """
        This function is called to reset the view without destroying the object
        """
        # background
        self.background = load_texture(f"{RESOURCE_PATH}backgrounds/Paper.png")

        # button manager
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

        #music
        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])

        # stats from previous games or from current session
        if stat_tracker != None:
            self.accuracy = f"{stat_tracker.percentage():.2f}"
            self.WPM = int(stat_tracker.wpm())
            self.letters_struggle = stat_tracker.struggle_letters()
            # aps is used to replace the apstrophes when we write to the file
            aps = "'"
            # saves the current data to the save file
            with open(f"{RESOURCE_PATH}save\\save.txt", 'a') as save_file:
                # converting a list to string and replacing all the extra characters
                save_file.write(f"\n{self.WPM},{self.accuracy},{str(self.letters_struggle).replace(',','').replace(' ','').replace('[','').replace(']','').replace(f'{aps}','')}")
        else:
            # if the player is not coming from the training session displays the previous scores
            with open(f"{RESOURCE_PATH}save\\save.txt") as save_file:
                lines = save_file.readlines()
                self.WPM, self.accuracy, self.letters_struggle = lines[-1].split(",")
                self.letters_struggle = list(self.letters_struggle)
                

    def on_draw(self):
        start_render()
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()
        # draws the score on the screen in a human readable way
        if self.WPM != None:
            draw_text(f"WPM: {self.WPM}", self.window.width / 4, self.window.height * .75, color.GREEN, 24, 800, "center", "Ultra")  # TODO This needs to receive a score from stattracker.py "Score: 0" is a placeholder.
            draw_text(f"Percentage: {self.accuracy}", self.window.width / 4, self.window.height * .55, color.GREEN, 24, 800, "center", "Ultra")
            draw_text(f"Adjusted WPM: {float(self.WPM) * float(self.accuracy)/100}", self.window.width / 4, self.window.height * .4, color.GREEN, 24, 800, "center", "Ultra")
            draw_text(f"Letters You Struggled With: {self.letters_struggle}", self.window.width / 4, self.window.height * .25, color.GREEN, 24, 800, "center", "Ultra")

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def destroyButtons(self):
        """
        Used to stop buttons from being clicked while view not in current buffer
        """
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol = symbol, modifier = modifiers)