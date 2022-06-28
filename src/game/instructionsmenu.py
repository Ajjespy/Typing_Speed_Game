import arcade
import arcade.gui
import game.constants as const
import game.controller as controller
from game.constants import RESOURCE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH
from random import randint
from game.tumbleweed import Tumbleweed

class InstructionsMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = True
        self.max_x = self.window.width
        self.max_y = self.window.height
        self.tumbleweed_present = False
        self.turn_speed = -75
        self.tumbleweed_path_list = [2,0.5,0.25,0,-0.25,-0.5,-2]
        self.Tim = arcade.Sprite(f"{const.RESOURCE_PATH}/enemy_sprites/Friendly Tim.png", 0.75)
        self.Tim.center_x = 150
        self.Tim.center_y = 150
        self.speach = """
        
        Howdy partner! It’s been a while since this here town has gotten any visitors just to let you know, this town has gotten a strange tradition for when we get visitors. We have a town-wide paintball fight!

Here have one of our special model paintball guns. The gunsmith calls this one “The Keyboard”. If you are unfamiliar with how “The Keyboard” works, you should go down to that there shooting range to LEARN how to work that gun. It would be a shame if you didn’t know how to work your gun when the GAME begins.

After practicing and participating in the town paintball match, there will be a SCORE board you can check out. Can you be the rootinest tootinest cowboy this town has ever seen?

        """

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
            const.SFX_HANDLER.play_sfx()
        
        self.vBox.add(backButton.with_space_around(right = 80, left = 80))

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x = "center", anchor_y = "center", align_x=660, align_y=-350, child = self.vBox))

        self.manager.add(arcade.gui.UIPadding(child=self.vBox, bg_color=(0, 0, 0, 0)))

        const.MUSIC_HANDLER.update_music_list([f"{const.RESOURCE_PATH}/music/a-gentle-breeze-wind-4-14681.mp3",])  # add music here
        const.MUSIC_HANDLER.play_song()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()
        arcade.draw_text(self.speach, 0, self.max_y, arcade.color.BLACK, 24, self.max_x, "center", "Ultra")  # TODO Create actual instructions.
        self.Tim.draw()
        if self.tumbleweed_present:
            self.tumbleweed.draw()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        self.generate_tumbleweed()
        if self.tumbleweed_present:
            self.tumbleweed.update()

    def generate_tumbleweed(self):

        tumble_chance = randint(0,500)

        scale = self.max_x / 960

        if self.tumbleweed_present == False:
            if tumble_chance == 500:
                self.tumbleweed = Tumbleweed(0, (25 * scale), 0.25, self.tumbleweed_path_list, 3, 15, self.turn_speed)
                self.tumbleweed_present = True
        else:
            if self.tumbleweed.center_x > self.max_x + 300:
                self.tumbleweed = None
                self.tumbleweed_present = False

    def destroyButtons(self):
        self.manager.disable()

    def on_key_press(self, symbol: int, modifiers: int):
        controller.Controller.get_key_press(self, symbol = symbol, modifier = modifiers)