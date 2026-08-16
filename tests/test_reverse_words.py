import pytest

from textutils.reverse_words import reverse_words


def test_reverses_single_spaced_words():
    assert reverse_words("eins zwei drei") == "drei zwei eins"


def test_empty_string_returns_empty_string():
    assert reverse_words("") == ""


def test_single_word_unchanged():
    assert reverse_words("hallo") == "hallo"


def test_collapses_multiple_whitespace_to_single_space():
    assert reverse_words("  ein   Test  ") == "Test ein"


def test_splits_on_tabs_and_newlines():
    assert reverse_words("a\tb\nc") == "c b a"


def test_whitespace_only_returns_empty_string():
    assert reverse_words("   ") == ""


def test_null_bytes_are_kept_within_words():
    assert reverse_words("a\x00 b\x00c") == "b\x00c a\x00"


def test_control_characters_do_not_raise():
    assert reverse_words("one\x01 two\x02") == "two\x02 one\x01"


def test_very_long_string():
    long_text = "x" * 1_000_000 + " y" * 500_000
    assert reverse_words(long_text) == (" y" * 500_000)[1:] + " " + ("x" * 1_000_000)


@pytest.mark.parametrize("bad", [None, 42, 3.14, b"bytes", ["a", "b"]])
def test_non_str_input_raises_type_error(bad):
    with pytest.raises(TypeError):
        reverse_words(bad)
