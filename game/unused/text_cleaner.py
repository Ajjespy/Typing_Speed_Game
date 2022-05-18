"""
This program clean profanity and other terms from a csv file. 
It is not perfect as it can only remove what is in the given profanity list.
If you find that it has missed a word or term, please let Andrew know.
Currently it only cleans the data in index[1].
"""

profanity = open('openProfanityList.csv', 'r')
original_list = open('words_with_pos_dirty.csv', 'r')

def gather_profanity():

    profanity = [] # creates empty list to store all instances of profanity

    with open('openProfanityList.csv') as profanity_list:
        for lines in profanity_list:
            profanity.append(lines.replace(' ','').replace('\n', '')) # removes all whitespace and \n characters

    return profanity

def clean(profanity, cwl):
    index = 0
    with open('words_with_pos_dirty.csv') as original_list:

        for lines in original_list:
            line = lines.split(',') # breaking up csv values
            curr_word = line[1].replace(' ','') # cleaning whitespace

            if curr_word not in profanity:
                cwl.writelines(f'{index},{line[1]},{line[2]}')
                index += 1
       

def main():
    cwl = open('clean_word_list.csv', 'w')
    profanity = gather_profanity()
    clean(profanity, cwl)

if __name__ == "__main__":
    main()