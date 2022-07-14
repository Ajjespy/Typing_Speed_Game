import time

class StatTracker():

    def __init__(self):
        self.list_of_user_words = []
        self.list_of_words = []
        self.start_time = 0
        self.end_time = 0

    def percentage(self):
        """
        This function returns the accuracy of the users input
        """
        missed_count = 0
        char_count = 0
        list_of_characters_one = []
        list_of_user_characters_one = []

        # counts the total number of letters from list of words
        for i in range(0, len(self.list_of_words)):
            list_of_characters_one = list_of_characters_one + list(self.list_of_words[i])
            list_of_user_characters_one = list_of_user_characters_one + list(self.list_of_user_words[i])

        # counts total number of letters missed by user
        for i in range(0, len(list_of_characters_one)):
            if list_of_user_characters_one[i] != list_of_characters_one[i]:
                missed_count += 1
        
        char_count = len(list_of_characters_one)

        if char_count == 0:
            return 0

        # calculate letters missed
        # returns float value
        raw_accuracy = (char_count - missed_count) / char_count
        # calculate actual accuracy percentage
        self.user_accuracy = raw_accuracy * 100

        return self.user_accuracy
      
    def wpm(self):
        """
        This function returns the wpm of the user
        """
        # time is in seconds
        typing_time = self.end_time - self.start_time

        if typing_time == 0:
            return 0
        # convert time to minutes
        time_in_minutes = float(typing_time / 60)

        wordspm = len(self.list_of_user_words) / time_in_minutes

        return wordspm

    def struggle_letters(self):
        """
        This function returns the letters that the player struggled the most with
        """
        self.missed_letters = {}
        self.struggle_list = []
        self.list_of_characters = []
        self.list_of_user_characters = []
        
        # loop iterates through list_of_words
        # appends each character to a new list as its own element
        for i in range(0, len(self.list_of_words)):
            self.list_of_characters = self.list_of_characters + list(self.list_of_words[i])
            self.list_of_user_characters = self.list_of_user_characters + list(self.list_of_user_words[i])
        
        # loop compares 2 lists finding discrepancies
        # each missing letter is added to a dictionary as a key and the count of the missing letter is the value 
        for i in range(0, len(self.list_of_characters)):
            if self.list_of_user_characters[i] != self.list_of_characters[i]:
                if self.list_of_characters[i] in self.missed_letters:
                    self.missed_letters[self.list_of_characters[i]] += 1
                else:
                    self.missed_letters[self.list_of_characters[i]] = 1
        
        # searches through dictionary to find letters
        # missed 2 or more times, then the letter is added to a list named struggle_list
        for key in self.missed_letters:
            item = self.missed_letters[key]
            if item >= 2:
                self.struggle_list.append(key)
        
        return self.struggle_list
                 
    def add_word(self, word):
        """
        This function adds the words the user is supposed to type to the word list
        """
        self.list_of_words.append(word)

    def set_start(self):
        """
        This function sets the start time
        """
        self.start_time = time.time()

    def set_end(self):
        """
        This function sets the end time
        """
        self.end_time = time.time()

    def add_user_word(self, word):
        """
        This function adds words that user has typed
        """
        self.list_of_user_words.append(word)
