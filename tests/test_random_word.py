import string
from speed_typing.game.random_word import RandomWord

def test_random_word():
    assert type(RandomWord.get_random_chars) == string