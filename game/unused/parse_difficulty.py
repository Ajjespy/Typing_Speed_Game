"""
Assigns a difficulty to each word based on the length and position of the letters on the keyboard.

This can be modified to balance the game, but when run it will create a new file under "game",
which must be moved to resources.
"""

import statistics as stats
original_list = open('game/resources/clean_word_list.csv', 'r')

###########################################################################################
# Use these to modify the relative weight of the length/key location. This is a multiplier!
WORD_LENGTH_WEIGHT = 1
KEY_LOCATION_WEIGHT = 1
###########################################################################################


def gather_words():

    words = []

    for line in original_list:
        words.append(line.replace(' ','').replace('\n', '')) # removes all whitespace and \n characters

    return words


def parse():
    list = gather_words()

    with open("clean_word_list_with_difficulty.csv", "w") as test_file: 
        for line in list:
            
            parts = line.split(",")
            index = parts[0]
            word = parts[1]
            pos = parts[2]

            difficulty = get_difficulty(word)

            new_line = index + "," + word + "," + pos + "," + str(difficulty) + "\n"

            test_file.writelines(new_line)


def get_difficulty(word): # This sets all of the logic for word difficulty
    difficulty = 0
    
    if type(word) is str:
        characters = list(word)

    difficulty += len(characters) * WORD_LENGTH_WEIGHT

    for char in characters:
        if char in ["A", "S", "D", "F", "G", "H", "J", "K", "L"]:
            difficulty += 0 * KEY_LOCATION_WEIGHT
        elif char in ["W", "E", "R", "T", "Y", "U", "I", "O"]:
            difficulty += 1 * KEY_LOCATION_WEIGHT
        elif char in ["Q", "P"]:
            difficulty += 1.5 * KEY_LOCATION_WEIGHT
        elif char in ["C", "V", "B", "N", "M"]:
            difficulty += 2 * KEY_LOCATION_WEIGHT
        elif char in ["Z", "X",]:
            difficulty += 2.5 * KEY_LOCATION_WEIGHT
        else: difficulty += 0
    
    return difficulty


def analyze_file():

    difficulty_list = []

    with open("clean_word_list_with_difficulty.csv") as test_file:
        for line in test_file:
            parts = line.split(",")
            difficulty_list.append(float(parts[3]))

    print(f"The mean difficulty is: {stats.mean(difficulty_list)}")
    print(f"The median difficulty is: {stats.median(difficulty_list)}")
    print(f"The max difficulty is: {max(difficulty_list)}")
    print(f"The min difficulty is: {min(difficulty_list)}")


def main():
    parse()
    analyze_file()

if __name__ == "__main__":
    main()