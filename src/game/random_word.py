# TODO
# Implement a difficulty system.
# Shorter words for practice mode.
from random import randint
from linecache import clearcache, getline
from game.constants import RESOURCE_PATH, LETTERS_BY_ROW

FILE_NAME = RESOURCE_PATH + "clean_word_list_with_difficulty.csv"
DIFF_1 = RESOURCE_PATH + "word_files/diff_1.csv"
DIFF_2 = RESOURCE_PATH + "word_files/diff_2.csv"
DIFF_3 = RESOURCE_PATH + "word_files/diff_3.csv"
DIFF_4 = RESOURCE_PATH + "word_files/diff_4.csv"
DIFF_5 = RESOURCE_PATH + "word_files/diff_5.csv"
DIFF_6 = RESOURCE_PATH + "word_files/diff_6.csv"
DIFF_7 = RESOURCE_PATH + "word_files/diff_7.csv"
DIFF_8 = RESOURCE_PATH + "word_files/diff_8.csv"


class RandomWord:
    """
    This class is used to get a random word or characters as a string.

    Static Methods: 
    get_random_chars() 
    get_random_word()
    """

    def set_word(difficulty):
        clearcache()

        if difficulty == 1:
            file_name = DIFF_1
        if difficulty == 2:
            file_name = DIFF_2
        if difficulty == 3:
            file_name = DIFF_3
        if difficulty == 4:
            file_name = DIFF_4
        if difficulty == 5:
            file_name = DIFF_5
        if difficulty == 6:
            file_name = DIFF_6
        if difficulty == 7:
            file_name = DIFF_7
        if difficulty == 8:
            file_name = DIFF_8

        with open(file_name, "r") as f:
            length = len(f.readlines())

        line = getline(file_name, randint(1, length))
        parts = line.split(",")
        return parts[1].strip()

        
    def get_word(difficulty = 3) -> str:
        """
        Gets a random word in difficulty range.

        Parameters:
        difficulty (int): int 1-8

        Returns:
        str: random word
        """
        if difficulty > 8:
            raise OverflowError

        word = RandomWord.set_word(difficulty)
        return word


    def get_random_chars(length = 1, lower_case = True, row = "ALL") -> str:
        """
        Gets a string of random characters from all or specific keyboard rows.
        
        Parameters:
        number (int): the number of characters that will be returned
        upper_case (bool): return will be upper case if true
        row (str): Specifies which row the letters will be drawn from
                    must be "TOP", "MIDDLE", "TOP_MIDDLE", or "BOTTOM" 
                    Default is "ALL"

        Returns:
        str: returns string of characters
        """

        letters = ""
        for i in range(length):
            letters += LETTERS_BY_ROW[row][randint(0, len(LETTERS_BY_ROW[row]) - 1)]

        if lower_case:
            return letters.lower() # TODO allow string to have variable numbers of capitals mixed in
        else:
            return letters


# print(RandomWord.get_random_chars(10, True))
# print(RandomWord.get_word(2))
