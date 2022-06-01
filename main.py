from arcade import Window, set_background_color, run
from arcade.color import ARSENIC
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from game.mainmenu import MainMenu

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable = False, fullscreen = True)
    set_background_color(ARSENIC)
    game_view = MainMenu()
    game_view.setup()
    window.show_view(game_view)
    run()

if __name__ == "__main__":
    main()
