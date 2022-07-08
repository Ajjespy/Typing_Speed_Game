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
    """
    This function handles key presses for every view
    """
    # changes the texture of keyboard sprites if they are pressed down
    if symbol >= 97 and symbol < 123 and not unpress:
        try:
            #if numbers are used need to convertLetters[chr(symbol).upper()] + 9
            director.keyboard_sprites[convertLetters[chr(symbol).upper()] - 1].texture = load_texture(f"{RESOURCE_PATH}keys_pressed/{chr(symbol - 97 + 65)}_Key_Light.png")
        except:
            pass

    # changes the texture of keyboard sprites if they are not pressed down
    if symbol >= 97 and symbol < 123 and unpress:
        try:
            director.keyboard_sprites[convertLetters[chr(symbol).upper()] - 1].texture = load_texture(f"{RESOURCE_PATH}keys_unpressed/{chr(symbol - 97 + 65)}_Key_Dark.png")
        except:
            pass

    # changes the texture of keyboard sprites if they are pressed down
    if (symbol == key.LSHIFT or symbol == key.RSHIFT) and not unpress:
        try:
            director.keyboard_sprites[len(director.keyboard_sprites) - 1].texture = load_texture(f"{RESOURCE_PATH}keys_pressed/Shift_Alt_Key_Light.png")
        except:
            pass

    # changes the texture of keyboard sprites if they are not pressed down
    if (symbol == key.LSHIFT or symbol == key.RSHIFT) and unpress:
        try:
            director.keyboard_sprites[len(director.keyboard_sprites) - 1].texture = load_texture(f"{RESOURCE_PATH}keys_unpressed/Shift_Alt_Key_Dark.png")
        except:
            pass
        
    # pressing escape will quit the game
    if symbol == key.ESCAPE:
        exit()

    # pressing delete will take you back to main menu
    if symbol == key.DELETE:
        on_change_view(director, 0)
    

def on_change_view(director, view, difficulty = "ALL", stat_tracker = None):
    """
    This method will change which window the user is looking at.
    Args:
    director - Current View
    view - int {0: MainMenu(), 1: TrainingInstructions(), 2: Training(), 3: ScoreMenu(), 4: InstructionsMenu(), 5: LevelGenerator(), 6: TrainingMenu()}
    """
    # stores the views for quick calling
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
            # if the view is the training view then you have to specify difficulty
            gameView.setup(difficulty = difficulty)
            if director.buttons:
                director.destroyButtons()
            director.window.show_view(gameView)

        elif view == 3:
            # if the view is stat view then we want to display the stats from the previous game/training session
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

