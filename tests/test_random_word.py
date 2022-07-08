from game.random_word import RandomWord
import game.constants as const
import pytest

def test_get_word_gives_string(difficulty=3):
    for _ in range(difficulty):
        word = RandomWord.get_word(difficulty)
        assert type(word) is str

def test_get_word_difficulty_in_range():
    with pytest.raises(OverflowError):
        assert RandomWord.get_word(9)
    
    for i in range(1, 9):
        test_get_word_gives_string(i)

def test_get_random_chars_gives_string():
    assert type(RandomWord.get_random_chars()) is str

def test_get_random_chars_gives_correct_row():
    top = RandomWord.get_random_chars(100, row="TOP")
    middle = RandomWord.get_random_chars(100, row="MIDDLE")
    bottom = RandomWord.get_random_chars(100, row="BOTTOM")
    top_middle = RandomWord.get_random_chars(100, row="TOP_MIDDLE")

    for char in top:
        assert char.upper() in const.LETTERS_BY_ROW["TOP"]
    for char in middle:
        assert char.upper() in const.LETTERS_BY_ROW["MIDDLE"]
    for char in bottom:
        assert char.upper() in const.LETTERS_BY_ROW["BOTTOM"]
    for char in top_middle:
        assert char.upper() in const.LETTERS_BY_ROW["TOP_MIDDLE"]