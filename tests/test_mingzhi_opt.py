import pytest
import yaml

from pathlib import Path

from bomisspell.mingzhi import get_mingzhi_options
from bomisspell.utils import parse_syl

@pytest.fixture(scope="module")
def mingzhi_mapping():
    return {
        'སྔ': ['ལྔ', 'རྔ'],
        'ཇ': ['བྱ', 'ལྗ', 'རྗ'],
        'སྐྲ': ['ཀྲ','ཏྲ','པྲ','སྤྲ','ཊ']
    }

def test_mingzhi_with_vowel_options(mingzhi_mapping):
    syl = 'འཇུག'
    expected_options = ['འབྱུག་', 'འལྗུག་', 'འརྗུག་']
    syl_parts = parse_syl(syl)
    options = get_mingzhi_options(syl_parts, mingzhi_mapping)
    assert expected_options == options

def test_mingzhi_without_vowel_options(mingzhi_mapping):
    syl = 'བསྔགས'
    expected_options = ['བལྔགས་', 'བརྔགས་']
    syl_parts = parse_syl(syl)
    options = get_mingzhi_options(syl_parts, mingzhi_mapping)
    assert expected_options == options

def test_mingzhi_without_mapping(mingzhi_mapping):
    syl = 'ཐུགས'
    syl_parts = parse_syl(syl)
    expected_options = []
    options = get_mingzhi_options(syl_parts, mingzhi_mapping)
    assert expected_options == options

def test_mingzhi_only():
    syl = 'སྐྲ'
    mingzhi_map = yaml.safe_load(Path('./resources/mingzhi_mapping.yaml').read_text(encoding='utf-8'))
    syl_parts = parse_syl(syl)
    expected_options = ['ཀྲ་','ཏྲ་','པྲ་','སྤྲ་','ཊ་']
    options = get_mingzhi_options(syl_parts, mingzhi_map)
    assert expected_options == options