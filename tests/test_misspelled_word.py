import pytest

from bomisspell.exceptions import HomophoneNotFound
from bomisspell.option_generator import get_misspelled_word


def test_misspelled_word():
    mingzhi_mapping = {
        'པ': [],
        'ཇ': ['བྱ', 'ལྗ', 'རྗ'],
    }
    word = 'འཇུག་པ་'
    expected_options = ['ཇུག་པ་', 'གཇུག་པ་', 'དཇུག་པ་', 'བཇུག་པ་', 'མཇུག་པ་', 'འབྱུག་པ་', 'འལྗུག་པ་', 'འརྗུག་པ་', 'འཇུགས་པ་', 'འཇུགད་པ་']
    options = get_misspelled_word(word, mingzhi_mapping)
    assert expected_options == options

def test_misspelled_word():
    word = 'བུད་'
    expected_options = ['གབུད་', 'དབུད་', 'བབུད་', 'མབུད་', 'འབུད་', 'སྦུད་', 'ལྦུད་', 'རྦུད་', 'བུདས་', 'བུདད་']
    options = get_misspelled_word(word)
    assert expected_options == options

def test_no_homophone():
    with pytest.raises(HomophoneNotFound):
        word = 'ཕ་'
        options = get_misspelled_word(word)
        