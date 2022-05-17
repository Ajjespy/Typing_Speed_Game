from arcade import Window, set_background_color, run
from arcade.color import ARSENIC
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from game.display import Display

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable = True, fullscreen = True)
    set_background_color(ARSENIC)
    game_view = Display()
    game_view.setup()
    window.show_view(game_view)
    run()

if __name__ == "__main__":
    main()