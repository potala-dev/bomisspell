from bomisspell.option_generator import get_misspelled_opt
from bomisspell.utils import parse_syl

def test_misspelled_opt():
    syl_parts = parse_syl('འཇུག')
    expected_options = ['ཇུག་', 'གཇུག་', 'དཇུག་', 'བཇུག་', 'མཇུག་', 'འབྱུག་', 'འལྗུག་', 'འརྗུག་', 'འཇུགས་', 'འཇུགད་', 'འཇུག་']
    options = get_misspelled_opt(syl_parts)
    assert expected_options == options