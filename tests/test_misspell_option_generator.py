from misspell_generator.option_generator import get_misspelled_opt, parse_syl


def test_misspelled_opt():
    syl_parts = parse_syl('འཇུག')
    expected_options = ['གཇུགས་', 'དཇུགད་', 'མཇུགད་', 'ཇུག་', 'འཇུག་', 'ཇུགས་', 'གཇུགད་', 'བཇུགད་', 'བཇུགས་', 'བཇུག་', 'གཇུག་', 'མཇུགས་', 'དཇུགས་', 'ཇུགད་', 'དཇུག་', 'མཇུག་']
    options = get_misspelled_opt(syl_parts)
    assert frozenset(expected_options) == frozenset(options)