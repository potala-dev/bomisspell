import pytest

from bomisspell.option_generator import get_misspelled_opt
from bomisspell.utils import parse_syl

@pytest.fixture(scope="module")
def mingzhi_mapping():
    return {
        'སྔ': ['ལྔ', 'རྔ'],
        'ཇ': ['བྱ', 'ལྗ', 'རྗ'],
    }
def test_misspelled_opt(mingzhi_mapping):
    syl_parts = parse_syl('འཇུག')
    expected_options = ['ཇུག་', 'གཇུག་', 'དཇུག་', 'བཇུག་', 'མཇུག་', 'འབྱུག་', 'འལྗུག་', 'འརྗུག་', 'འཇུགས་', 'འཇུགད་']
    options = get_misspelled_opt(syl_parts, mingzhi_mapping)
    assert expected_options == options