from bomisspell.option_generator import get_misspelled_word


def test_misspelled_word():
    mingzhi_mapping = {
        'པ': [],
        'ཇ': ['བྱ', 'ལྗ', 'རྗ'],
    }
    word = 'འཇུག་པ་'
    expected_options = ['ཇུག་པ་', 'གཇུག་པ་', 'དཇུག་པ་', 'བཇུག་པ་', 'མཇུག་པ་', 'འབྱུག་པ་', 'འལྗུག་པ་', 'འརྗུག་པ་', 'འཇུགས་པ་', 'འཇུགད་པ་', 'འཇུག་པ་']
    options = get_misspelled_word(word, mingzhi_mapping)
    assert expected_options == options

def test_misspelled_word():
    mingzhi_mapping = {
        'ཇ': ['བྱ', 'ལྗ', 'རྗ'],
    }
    word = 'འཇུག་'
    expected_options = ['ཇུག་', 'གཇུག་', 'དཇུག་', 'བཇུག་', 'མཇུག་', 'འབྱུག་', 'འལྗུག་', 'འརྗུག་', 'འཇུགས་', 'འཇུགད་', 'འཇུག་']
    options = get_misspelled_word(word, mingzhi_mapping)
    assert expected_options == options