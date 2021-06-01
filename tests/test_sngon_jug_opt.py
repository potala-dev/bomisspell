from bomisspell.sgnon_jung import get_sngon_jug_options
from bomisspell.utils import parse_syl

def test_sngon_jug_opt():
    syl = 'འཇུག'
    syl_parts = parse_syl(syl)
    excepted_options = ['ཇུག་', 'གཇུག་', 'དཇུག་', 'བཇུག་', 'མཇུག་']
    options = get_sngon_jug_options(syl_parts)
    assert excepted_options == options

def test_mingzhi_only():
    syl = 'ཉ'
    syl_parts = parse_syl(syl)
    excepted_options = []
    options = get_sngon_jug_options(syl_parts)
    assert excepted_options == options