from os import path
from arcade import load_font

SCREEN_WIDTH = int(1920 / 2)
SCREEN_HEIGHT = int(1080 / 2)
SCREEN_TITLE = "Typing Game"
RESOURCE_PATH = f"{path.dirname(path.abspath(__file__))}/resources/"
FONT = load_font(f"{RESOURCE_PATH}westernfont.ttf")

convertLetters = dict()
alphabet = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
for i in range(0, len(alphabet)):
    convertLetters[alphabet[i]] = i + 1

LETTERS_BY_ROW = {
        "TOP": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], # Keyboard top row
        "MIDDLE": ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        "TOP_MIDDLE": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                "A", "S", "D", "F", "G", "H", "J", "K", "L"],
        "BOTTOM": ["Z", "X", "C", "V", "B", "N", "M"],
        "ALL": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A",
                "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
        }