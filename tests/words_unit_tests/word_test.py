from word_db import Word

words = Word()

def test_add_word():
    assert words.add_word('Firefighter', 'Profession which workers fight against fires') == True

def test_get_word():
    assert words.get_word() == 'Firefighter'

def test_get_tip():
    assert words.get_tip('Firefighter') == 'Profession which workers fight against fires'

