import arcade

screen_width = 1982
screen_height = 1080

class display(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.background = arcade.load_texture(".\Typing_Speed_Game\resources\TitleScreen.png")

window = display(screen_width,screen_height,"Wild West")
window.setup()
arcade.run()