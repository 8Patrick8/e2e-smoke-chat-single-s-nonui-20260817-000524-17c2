from textutils.word_count import word_count


def test_word_count_single_word():
    assert word_count("Hallo") == 1


def test_word_count_multiple_words():
    assert word_count("eins zwei drei") == 3


def test_word_count_ac06_surrounding_whitespace():
    assert word_count("  ein   Test  ") == 2


def test_word_count_ac07_only_whitespace():
    assert word_count("   ") == 0


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_mixed_whitespace_separators():
    assert word_count("eins\tzwei\ndrei\rvier") == 4


def test_word_count_tabs_and_newlines_only():
    assert word_count("\t\n\r ") == 0


def test_word_count_null_bytes():
    assert word_count("ein\x00Test") == 1


def test_word_count_control_characters_are_not_separators():
    assert word_count("\x01\x02 ein \x03 Test \x04") == 5


def test_word_count_control_characters_only():
    assert word_count("\x01\x02\x03\x04") == 1


def test_word_count_very_long_string():
    text = (" " + "wort " * 250_000).strip()
    assert word_count(text) == 250_000
    assert len(text) > 1_000_000


def test_word_count_million_plus_characters_single_word():
    assert word_count("a" * 1_000_001) == 1


def test_word_count_unicode_whitespace():
    assert word_count("ein\u00a0Test\u2003zwei") == 3


def test_word_count_non_str_raises_typeerror():
    for bad_input in (None, 42, 3.14, ["ein", "Test"], b"ein Test", {"a": 1}):
        try:
            word_count(bad_input)  # type: ignore[arg-type]
        except TypeError:
            pass
        else:
            raise AssertionError(f"word_count({bad_input!r}) should raise TypeError")
