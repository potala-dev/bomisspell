from bomisspell.utils import parse_syl
from bomisspell.yang_jug import get_yang_jug_options

def test_yang_jug_opt():
    syl = 'འཇུག'
    syl_parts = parse_syl(syl)
    expected_options = ['འཇུགས་', 'འཇུགད་']
    options = get_yang_jug_options(syl_parts)
    assert expected_options == options

def test_without_jes_jug():
    syl = 'བདེ'
    syl_parts = parse_syl(syl)
    expected_options = []
    options = get_yang_jug_options(syl_parts)
    assert expected_options == options