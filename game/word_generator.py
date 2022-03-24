"""
Class for the word generator
"""

import random


class WordGenerator:

    # Method to get a new word from the generator
    def __init__(self, word_db, **kwargs) -> None:
        self._word_bank = word_db
        self._generated_word = ""
        self._scrambled_word = []

        # Getting a new word.
        self.get_new_word()

    # Method used internally to transform a list of letters to a single complete string
    def _list_to_string(self, list_object: list) -> str:
        string = ""
        for letter in list_object:
            string += letter
        return string

    # Method to convert a list of letters into a single string
    def get_new_word(self) -> str:
        self._generated_word = self._word_bank.get_word()
        return self._generated_word

    # Method to get the scrambled word
    def get_scrambled_word(self) -> str:
        if len(self._scrambled_word) > 1:
            self._scrambled_word = []

        for letter in self._generated_word:
            self._scrambled_word.append(letter)
        random.shuffle(self._scrambled_word)
        return_word = self._list_to_string(self._scrambled_word)
        return return_word

    # Method to get the original word before being scrambled
    def get_original_word(self) -> str:
        return self._generated_word

    # Get the tip of the current scrambled word
    def get_tip(self) -> str:
        return self._word_bank.get_tip(self._generated_word)

    # Returns the word bank
    def get_word_bank(self):
        return self._word_bank
