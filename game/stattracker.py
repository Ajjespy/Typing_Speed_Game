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
        word_count = 0
        self.list_of_words_one = []
        self.list_of_user_words_one = []
        self.list_of_characters_one = []
        self.list_of_user_characters_one = []

        # counts the total number of letters from list of words
        for i in range(0, len(self.list_of_words_one)):
            self.list_of_characters_one = self.list_of_characters_one + list(self.list_of_words_one[i])
            word_count +=1
            self.list_of_user_characters_one = self.list_of_user_characters_one + list(self.list_of_user_words_one[i])

        # counts total number of letters missed by user
        for i in range(0, len(self.list_of_characters_one)):
            if self.list_of_user_characters_one[i] != self.list_of_characters_one[i]:
                missed_count += 1
        
        # calculate letters missed
        # returns float value
        raw_accuracy = word_count - missed_count / word_count
        # calculate actual accuracy percentage
        self.user_accuracy = raw_accuracy * 100

        return self.user_accuracy
      

    def wpm(self):
        """
        This function returns the wpm of the user
        """
        # time is in seconds
        self.typing_time = self.end_time - self.start_time
        # convert time to minutes
        self.time_in_minutes = self.typing_time / 60

        self.wpm = len(self.list_of_user_words)/ self.time_in_minutes

        return self.wpm + 20

    def struggle_letters(self):
        """
        This function returns the letters that the player struggled the most with
        """
        self.missed_letters = {}
        self.list_of_user_words = []
        self.list_of_words = []
        self.struggle_list = []
        self.list_of_characters = []
        self.list_of_user_characters = []

        for i in range(0, len(self.list_of_words)):
            self.list_of_characters = self.list_of_characters + list(self.list_of_words[i])
            self.list_of_user_characters = self.list_of_user_characters + list(self.list_of_user_words[i])

        for i in range(0, len(self.list_of_characters)):
            if self.list_of_user_characters[i] != self.list_of_characters[i]:
                if self.list_of_characters[i] in self.missed_letters:
                    self.missed_letters[self.list_of_characters[i]] += 1
                else:
                    self.missed_letters[self.list_of_characters[i]] = 1

        for key in self.missed_letters:
            item = self.missed_letters[key]
            if item >= 2:
                self.struggle_list.append(key)
            else:
                pass
        
        return self.struggle_list
                 

    def add_word(self, word):
        """
        This function adds the words the user is supposed to type to the word list
        """
        self.word = word
        self.list_of_words.append(self.word)
        pass

    def set_start(self, time):
        """
        This function sets the start time
        """
        self.start_time = time.time()
        return self.start_time

    def set_end(self, time):
        """
        This function sets the end time
        """
        self.end_time = time.time()
        return self.end_time

    def add_user_word(self, word):
        """
        This function adds words that user has typed
        """
        self.word = word
        self.list_of_user_words.append(self.word)
        pass