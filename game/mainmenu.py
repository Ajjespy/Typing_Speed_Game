import arcade
import arcade.gui
import game.constants
from game.controller import controller


class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()


    def setup(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.vBox = arcade.gui.UIBoxLayout()

        self.background = arcade.load_texture(f"{game.constants.RESOURCE_PATH}TitleScreen.png")

        textureLearn = arcade.load_texture(f"{game.constants.RESOURCE_PATH}LearnButton.png")
        textureGame = arcade.load_texture(f"{game.constants.RESOURCE_PATH}GameButton.png")
        textureScores = arcade.load_texture(f"{game.constants.RESOURCE_PATH}ScoresButton.png")
        textureInstructions = arcade.load_texture(f"{game.constants.RESOURCE_PATH}InstructionsButton.png")
        textureQuit = arcade.load_texture(f"{game.constants.RESOURCE_PATH}QuitButton.png")

        learnButton = arcade.gui.UITextureButton(texture=textureLearn, scale= 0.5)
        gameButton = arcade.gui.UITextureButton(texture=textureGame, scale= 0.5)
        scoresButton = arcade.gui.UITextureButton(texture=textureScores, scale= 0.5)
        instructionButton = arcade.gui.UITextureButton(texture=textureInstructions, scale= 0.5)
        quitButton = arcade.gui.UITextureButton(texture=textureQuit, scale= 0.5)

        @learnButton.event("on_click")
        def on_click_texture_button(event):
            print("learn Button pressed", event)

        @gameButton.event("on_click")
        def on_click_texture_button(event):
            print("game Button pressed", event)

        @scoresButton.event("on_click")
        def on_click_texture_button(event):
            print("scores Button pressed", event)

        @instructionButton.event("on_click")
        def on_click_texture_button(event):
            print("instruction Button pressed", event)

        @quitButton.event("on_click")
        def on_click_texture_button(event):
            print("quit Button pressed", event)


        self.vBox.add(instructionButton.with_space_around(bottom=20))
        self.vBox.add(learnButton.with_space_around(bottom=20))
        self.vBox.add(gameButton.with_space_around(bottom=20))
        self.vBox.add(scoresButton.with_space_around(bottom=20))
        self.vBox.add(quitButton.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.vBox
            )
        )

    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
    