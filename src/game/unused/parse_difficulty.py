import statistics as stats
import numpy as np
original_list = open('game/resources/clean_word_list.csv', 'r')
difficulty_file = "game/resources/clean_word_list_with_difficulty.csv"

###########################################################################################
# Use these to modify the relative weight of the length/key location. This is a multiplier!
WORD_LENGTH_WEIGHT = 1.5
KEY_LOCATION_WEIGHT = 1
###########################################################################################


def gather_words():

    words = []

    with open(difficulty_file) as file:

        for line in file:
            words.append(line.replace(' ','').replace('\n', '')) # removes all whitespace and \n characters

    return words


def parse():
    list = gather_words()

    max = get_max(list)

    diff_1 = []
    diff_2 = []
    diff_3 = []
    diff_4 = []
    diff_5 = []
    diff_6 = []
    diff_7 = []
    diff_8 = []

    for line in list:
        
        parts = line.split(",")
        index = parts[0]
        word = parts[1]
        pos = parts[2]
        diff = get_difficulty(word)

        new_line = f"{index}, {word}, {pos}, {diff}\n"

        if diff < max / 10:
            diff_1.append(new_line)
        elif diff < (2 * max) / 10:
            diff_2.append(new_line)
        elif diff < (3 * max) / 10:
            diff_3.append(new_line)
        elif diff < (4 * max) / 10:
            diff_4.append(new_line)
        elif diff < (5 * max) / 10:
            diff_5.append(new_line)
        elif diff < (6 * max) / 10:
            diff_6.append(new_line)
        elif diff < (7 * max) / 10:
            diff_7.append(new_line)
        elif diff < (8 * max) / 10:
            diff_8.append(new_line)

    with open("diff_1.csv", "w") as file:
        for line in diff_1:
            file.writelines(line)
    with open("diff_2.csv", "w") as file:
        for line in diff_2:
            file.writelines(line)
    with open("diff_3.csv", "w") as file:
        for line in diff_3:
            file.writelines(line)
    with open("diff_4.csv", "w") as file:
        for line in diff_4:
            file.writelines(line)
    with open("diff_5.csv", "w") as file:
        for line in diff_5:
            file.writelines(line)
    with open("diff_6.csv", "w") as file:
        for line in diff_6:
            file.writelines(line)
    with open("diff_7.csv", "w") as file:
        for line in diff_7:
            file.writelines(line)
    with open("diff_8.csv", "w") as file:
        for line in diff_8:
            file.writelines(line)
    
def get_max(list):

    temp_list = []

    for line in list:
        
        parts = line.split(",")
        diff = parts[3]
        temp_list.append(int(diff))

    return np.amax(temp_list)

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



def main():
    parse()

if __name__ == "__main__":
    main()