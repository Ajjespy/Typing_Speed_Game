from arcade import load_texture, start_render, gui, exit, draw_text, draw_lrwh_rectangle_textured, View, color
from game.constants import RESOURCE_PATH, MUSIC_DICT, MUSIC_HANDLER, SFX_DICT, SFX_HANDLER
import game.controller as controller
from game.tumbleweed import Tumbleweed
from random import randint


class MainMenu(View):
    def __init__(self):
        super().__init__()
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        self.tumbleweed_present = False
        self.turn_speed = 75
        self.tumbleweed_path_list = [5,2,1,0,-1,-2,-5]
        self.tumblepoint = 0
        self.next_y = 0
        self.max_x = self.window.width
        self.max_y = self.window.height
        self.buttons = True
        self.saloon_name = """High Noon Typing Saloon"""



    def setup(self):
        self.manager = gui.UIManager()
        self.manager.enable()
        self.vBox = gui.UIBoxLayout(vertical=False)

        self.background = load_texture(f"{RESOURCE_PATH}TitleScreen.png")

        textureLearn = load_texture(f"{RESOURCE_PATH}LearnButton.png")
        textureLearnHovered = load_texture(f"{RESOURCE_PATH}LearnButtonHovered.png")
        textureGame = load_texture(f"{RESOURCE_PATH}GameButton.png")
        textureGameHovered = load_texture(f"{RESOURCE_PATH}GameButtonHovered.png")
        textureScores = load_texture(f"{RESOURCE_PATH}ScoresButton.png")
        textureScoresHovered = load_texture(f"{RESOURCE_PATH}ScoresButtonHovered.png")
        textureInstructions = load_texture(f"{RESOURCE_PATH}InstructionsButton.png")
        textureInstructionsHovered = load_texture(f"{RESOURCE_PATH}InstructionsButtonHovered.png")
        textureQuit = load_texture(f"{RESOURCE_PATH}QuitButton.png")
        textureQuitHovered = load_texture(f"{RESOURCE_PATH}QuitButtonHovered.png")

        learnButton = gui.UITextureButton(texture=textureLearn,texture_hovered=textureLearnHovered, scale= 0.5)
        gameButton = gui.UITextureButton(texture=textureGame,texture_hovered=textureGameHovered, scale= 0.5)
        scoresButton = gui.UITextureButton(texture=textureScores,texture_hovered=textureScoresHovered, scale= 0.5)
        instructionButton = gui.UITextureButton(texture=textureInstructions,texture_hovered=textureInstructionsHovered, scale= 0.5)
        quitButton = gui.UITextureButton(texture=textureQuit,texture_hovered=textureQuitHovered, scale= 0.5)

        # MUSIC_HANDLER.update_music_list([])
        MUSIC_HANDLER.play_song(MUSIC_DICT["main_theme"], loop=True)


        @learnButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 1)
            #print("learn Button pressed", event)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @gameButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 5)
            # print("game Button pressed", event)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @scoresButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 3)
            # print("scores Button pressed", event)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @instructionButton.event("on_click")
        def on_click_texture_button(event):
            controller.on_change_view(self, 4)
            # print("instruction Button pressed", event)
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])

        @quitButton.event("on_click")
        def on_click_texture_button(event):
            exit()
            SFX_HANDLER.play_sfx(SFX_DICT["whoosh"])


        self.vBox.add(instructionButton.with_space_around(right=80))
        self.vBox.add(learnButton.with_space_around(right=80))
        self.vBox.add(gameButton.with_space_around(right=80))
        self.vBox.add(scoresButton.with_space_around(right=80))
        self.vBox.add(quitButton)

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.vBox
            )
        )

        self.manager.add(
            gui.UIPadding(
                child=self.vBox,
                bg_color=(150,150,150)
            )
        )


    def on_draw(self):
        super().on_draw()
        start_render()
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        draw_text(self.saloon_name, (self.max_x/2)-225, self.max_y - 75, color.BLACK, 28, 425, "center", "Ultra")
        if self.tumbleweed_present:
            self.tumbleweed.draw()
        self.manager.draw()


    def on_update(self, delta_time: float):
        super().on_update(delta_time)

        self.generate_tumbleweed()
        if self.tumbleweed_present:
            self.tumbleweed.update()

    def destroyButtons(self):
        self.manager.disable()


    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol)
    

    def generate_tumbleweed(self):

        tumble_chance = randint(0,500)

        scale = self.max_x / 960

        if self.tumbleweed_present == False:
            if tumble_chance == 500:
                self.tumbleweed = Tumbleweed(self.max_x + 300, (70 * scale), 0.5, self.tumbleweed_path_list, -3, 15, self.turn_speed)
                self.tumbleweed_present = True
        else:
            if self.tumbleweed.center_x < -300:
                self.tumbleweed = None
                self.tumbleweed_present = False