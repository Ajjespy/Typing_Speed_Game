from arcade import load_texture, key, exit
from game.constants import RESOURCE_PATH, convertLetters
import game.trainingmenu
import game.traininginstructions
import game.training
import game.mainmenu
import game.scoremenu
import game.instructionsmenu
import game.levelGenerator


def get_key_press(director, symbol, unpress = False, modifier = None):
    
    if symbol == key.ESCAPE and not unpress:
        director.window.set_fullscreen(not director.window.fullscreen)

    if symbol in set(range(97, 123)) and not unpress:
        try:
            #if numbers are used need to convertLetters[chr(symbol).upper()] + 9
            director.keyboard_sprites[convertLetters[chr(symbol).upper()] - 1].texture = load_texture(f"{RESOURCE_PATH}keys_pressed/{chr(symbol - 97 + 65)}_Key_Light.png")
        except:
            pass

    if symbol in set(range(97, 123)) and unpress:
        try:
            director.keyboard_sprites[convertLetters[chr(symbol).upper()] - 1].texture = load_texture(f"{RESOURCE_PATH}keys_unpressed/{chr(symbol - 97 + 65)}_Key_Dark.png")
        except:
            pass

    if (symbol == key.LSHIFT or symbol == key.RSHIFT) and not unpress:
        try:
            director.keyboard_sprites[len(director.keyboard_sprites) - 1].texture = load_texture(f"{RESOURCE_PATH}keys_pressed/Shift_Alt_Key_Light.png")
        except:
            pass
    if (symbol == key.LSHIFT or symbol == key.RSHIFT) and unpress:
        try:
            director.keyboard_sprites[len(director.keyboard_sprites) - 1].texture = load_texture(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png")
        except:
            pass
        
    if (symbol == key.ESCAPE):
        exit()

    if (symbol == key.DELETE):
        on_change_view(director, 0)
    

def on_change_view(director, view, difficulty = "ALL", stat_tracker = None):
    """
    This method will change which window the user is looking at.
    Args:
    director - Window
    view - int {0: MainMenu(), 1: TrainingInstructions(), 2: Training(), 3: ScoreMenu(), 4: InstructionsMenu(), 5: LevelGenerator(), 6: TrainingMenu()}
    """

    viewDict = {
                0: game.mainmenu.MainMenu(),
                1: game.traininginstructions.TrainingInstructions(),
                2: game.training.Training(),
                3: game.scoremenu.ScoreMenu(),
                4: game.instructionsmenu.InstructionsMenu(),
                5: game.levelGenerator.LevelGenerator(),
                6: game.trainingmenu.TrainingMenu()
                }
                
    if view in viewDict:
        gameView = viewDict[view]
        
        if view == 2:
            gameView.setup(difficulty = difficulty)
            if director.buttons:
                director.destroyButtons()
            director.window.show_view(gameView)

        elif view == 3:
            gameView.setup(stat_tracker)
            if director.buttons:
                director.destroyButtons()
            director.window.show_view(gameView)

        elif view in viewDict.keys():
            gameView.setup()
            if director.buttons:
                director.destroyButtons()
            director.window.show_view(gameView)

        else:
            director.window.close_window()

