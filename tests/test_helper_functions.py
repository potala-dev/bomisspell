from bomisspell.utils import get_syls, parse_syl


def test_get_syls():
    word = "རང་བཞིན་"
    expected_syls = ['རང', 'བཞིན']
    syls = get_syls(word)
    assert expected_syls == syls

def test_get_syl_parts():
    syl = "བསྒྲིབས"
    expected_syl_parts = {
        'sngon_jug': 'བ',
        'mingzhi': 'སྒྲི',
        'jes_jug': 'བ',
        'yang_jug': 'ས'
    }
    syl_parts = parse_syl(syl)
    assert expected_syl_parts == syl_parts