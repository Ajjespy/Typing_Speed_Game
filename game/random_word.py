"""
This class is used to get a random word as a string from "clean_word_list.csv"
This currently unfinished, but will return a word as a string.
"""
# TODO
# Implement a difficulty system.
# Shorter words for practice mode.
# Get characters by keyboard row.

import random, linecache
from game.constants import RESOURCE_PATH

FILE_NAME = RESOURCE_PATH + "clean_word_list.csv"

class RandomWord:
    def __init__(self, level = 0) -> None:
       self.file = FILE_NAME
       self.difficulty = level
       self.word = None

    def manage_difficulty(self):
        pass

    def get_random_chars(length = 1, lower_case = False, row = "ALL"):
        """
        Gets a list of random characters.
        
        Parameters:
            number - the number of characters that will be returned -> INTEGER
            
            upper_case - return will be upper case if true -> BOOLEAN
            
            row - Specifies which row the letters will be drawn from
                    must be "TOP", "MIDDLE", "TOP_MIDDLE", or "BOTTOM" 
                    Default is "ALL"                                    -> STRING


        Returns: returns list of characters -> LIST of STRINGS
        """

        letters_by_row = {
            "TOP": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], # Keyboard top row

            "MIDDLE": ["A", "S", "D", "F", "G", "H", "J", "K", "L"],

            "TOP_MIDDLE": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L"],

            "BOTTOM": ["Z", "X", "C", "V", "B", "N", "M"],

            "ALL": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A",
                    "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
        }

        letters = ""
        for i in range(length):
            letters = letters + letters_by_row["ALL"][random.randint(0, len(letters_by_row[row]) - 1)]

        if lower_case:
            return letters
        else:
            return letters.upper()


    def get_word():
        """
        Gets a random line from the file.
        linecache reads the entire file to the cache, so if this hits performance too badly it can be reworked.

        Parameters: None

        Returns: random word -> STRING
        """
        line = linecache.getline(FILE_NAME, random.randint(0, 369038 - 1)) # 369038 is the last line in the file
        parts = line.split(",")
        return parts[1]

    def set_word(self):
        pass
