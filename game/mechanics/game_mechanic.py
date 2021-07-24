"""
Class setting up the mechanics of the game.
"""

from ScrambledWordsBot.game.word_generator import WordGenerator

class GameMechanic:
    def __init__(self) -> None:
        self._word_generator = WordGenerator()
        self._score = 0
        self._original_word = self._word_generator.get_original_word()
        self._scrambled_word = self._word_generator.get_scrambled_word()
        self._tries = 3
        self._skips = 3
        self._tips = 3

    def get_new_word(self):
        """
        Gets a new word from the database.
        """
        self._original_word = self._word_generator.get_new_word()
        self._scrambled_word = self._word_generator.get_scrambled_word()


    def check_word(self, word:str) -> bool:
        """
        Checks whether a typed word matches the current scrambled word and gives the user a score point if so.
        """
        if str(word) == str(self._original_word):
            self._score += 1
            return True

        else:   
            if not str(word) == str(self._original_word):
                self._tries -= 1
                return False
            return False

    def show_tip(self):
        """
        Returns the tip of the current scrambled word.
        """
        if self._tips < 1:
            return "You don't have more tips, sorry."
        else:
            self._tips -= 1
            return self._word_generator.get_tip()

    def skip_word(self):
        """
        Skips the current word.
        """
        if self._skips < 1:
            return "You don't have more skips, sorry."
        else:
            self._skips -= 1
            self.get_new_word()
            return True

    def get_scrambled_word(self) -> str:
        """
        Gets the current scrambled word.
        """
        return self._scrambled_word

    def get_original_word(self) -> str:
        """
        Gets the original word to be guessed.
        """
        return self._original_word

    def get_score(self) -> int:
        """
        Gets the player's current score.
        """
        return self._score

    def get_tries(self) -> int:
        """
         Gets the player's current remaining tries.
        """
        return self._tries

    def get_skips(self) -> int:
        """
        Gets the player's current remaining skips.
        """
        return self._skips

    def get_tips(self) -> int:
        """
        Gets the player's current remaining tips.
        """
        return self._tips

    # Method to reset the game
    def reset_game(self) -> None:
        """
        Resets the game.
        """
        self._tries = 3
        self._tips = 3
        self._skips = 3
        self._score = 0
        self.get_new_word()
