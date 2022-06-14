from tkinter import VERTICAL
import arcade
import arcade.gui
import game.constants
import game.controller


class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()


    def setup(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.vBox = arcade.gui.UIBoxLayout(vertical=False)

        self.background = arcade.load_texture(f"{game.constants.RESOURCE_PATH}TitleScreen.png")

        textureLearn = arcade.load_texture(f"{game.constants.RESOURCE_PATH}LearnButton.png")
        textureLearnHovered = arcade.load_texture(f"{game.constants.RESOURCE_PATH}LearnButtonHovered.png")
        textureGame = arcade.load_texture(f"{game.constants.RESOURCE_PATH}GameButton.png")
        textureGameHovered = arcade.load_texture(f"{game.constants.RESOURCE_PATH}GameButtonHovered.png")
        textureScores = arcade.load_texture(f"{game.constants.RESOURCE_PATH}ScoresButton.png")
        textureScoresHovered = arcade.load_texture(f"{game.constants.RESOURCE_PATH}ScoresButtonHovered.png")
        textureInstructions = arcade.load_texture(f"{game.constants.RESOURCE_PATH}InstructionsButton.png")
        textureInstructionsHovered = arcade.load_texture(f"{game.constants.RESOURCE_PATH}InstructionsButtonHovered.png")
        textureQuit = arcade.load_texture(f"{game.constants.RESOURCE_PATH}QuitButton.png")
        textureQuitHovered = arcade.load_texture(f"{game.constants.RESOURCE_PATH}QuitButtonHovered.png")

        learnButton = arcade.gui.UITextureButton(texture=textureLearn,texture_hovered=textureLearnHovered, scale= 0.5)
        gameButton = arcade.gui.UITextureButton(texture=textureGame,texture_hovered=textureGameHovered, scale= 0.5)
        scoresButton = arcade.gui.UITextureButton(texture=textureScores,texture_hovered=textureScoresHovered, scale= 0.5)
        instructionButton = arcade.gui.UITextureButton(texture=textureInstructions,texture_hovered=textureInstructionsHovered, scale= 0.5)
        quitButton = arcade.gui.UITextureButton(texture=textureQuit,texture_hovered=textureQuitHovered, scale= 0.5)

        @learnButton.event("on_click")
        def on_click_texture_button(event):
            game.controller.Controller.on_change_view(self, 1)
            #print("learn Button pressed", event)


        @gameButton.event("on_click")
        def on_click_texture_button(event):
            #controller.on_change_view(self, 2)
            print("game Button pressed")

        @scoresButton.event("on_click")
        def on_click_texture_button(event):
            game.controller.Controller.on_change_view(self, 3)
            # print("scores Button pressed", event)

        @instructionButton.event("on_click")
        def on_click_texture_button(event):
            #controller.on_change_view(self, 4)
            print("instruction Button pressed", event)

        @quitButton.event("on_click")
        def on_click_texture_button(event):
            arcade.exit()


        self.vBox.add(instructionButton.with_space_around(right=80))
        self.vBox.add(learnButton.with_space_around(right=80))
        self.vBox.add(gameButton.with_space_around(right=80))
        self.vBox.add(scoresButton.with_space_around(right=80))
        self.vBox.add(quitButton)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.vBox
            )
        )

        self.manager.add(
            arcade.gui.UIPadding(
                child=self.vBox,
                bg_color=(0,0,0,75)
            )
        )

    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.manager.draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        game.controller.Controller.get_key_press(self, symbol)
    