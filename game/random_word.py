"""
This class is used to get a random word as a string from "clean_word_list.csv"
This currently unfinished, but will return a word as a string.
"""
# TODO
# Implement a difficulty system.
# Shorter words for practice mode.
# Get characters by keyboard row.

import random, linecache
from constants import RESOURCE_PATH

FILE_NAME = RESOURCE_PATH + "clean_word_list.csv"

class RandomWord:
    def __init__(self, level = 0) -> None:
       self.file = FILE_NAME
       self.difficulty = level
       self.word = None

    def manage_difficulty(self):
        pass

    def get_random_chars(self, number = 1, rows = None, upper_case = False):
        """
        Gets a list of random characters.
        
        Parameters:
            number - the number of characters that will be returned -> INTEGER
            rows - not yet implemented
            upper_case - return will be upper case if true -> BOOLEAN

        Returns: returns list of characters -> LIST of STRINGS
        """

        letters_by_row = {
            "TOP": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], # Keyboard top row

            "MIDDLE": ["A", "S", "D", "F", "G", "H", "J", "K", "L"],

            "BOTTOM": ["Z", "X", "C", "V", "B", "N", "M"],

            "ALL": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A",
                    "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
        }

        letters = []
        for i in range(number):
            letters.append(letters_by_row["ALL"][random.randint(0, len(letters_by_row["ALL"]) - 1)])

        return letters


    def get_word(self):
        """
        Gets a random line from the file.
        linecache reads the entire file to the cache, so if this hits performance too badly it can be reworked.

        Parameters: None

        Returns: random word -> STRING
        """
        line = linecache.getline(self.file, random.randint(0, 369038 - 1)) # 369038 is the last line in the file
        parts = line.split(",")
        return parts[1]

    def set_word(self):
        pass


# word = RandomWord()

# print(word.get_random_chars())

# print(word.get_word())