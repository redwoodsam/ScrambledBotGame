from ScrambledWordsBot.game.word_generator import WordGenerator

word_generator = WordGenerator()

def getting_word_test():
    assert word_generator.get_new_word()