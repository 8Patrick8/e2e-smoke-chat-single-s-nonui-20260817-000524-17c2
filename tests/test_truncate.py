import pytest

from textutils.truncate import truncate


def test_truncates_long_text():
    assert truncate("Hallo Welt", 5) == "Ha..."


def test_short_text_unchanged():
    assert truncate("kurz", 10) == "kurz"


def test_exact_length_unchanged():
    assert truncate("abc", 3) == "abc"


def test_empty_string_unchanged():
    assert truncate("", 5) == ""


def test_boundary_one_over():
    assert truncate("abcd", 3) == "..."


def test_min_max_len():
    assert truncate("Hallo", 3) == "..."


def test_max_len_less_than_three_raises_value_error():
    with pytest.raises(ValueError):
        truncate("abc", 2)


def test_negative_max_len_raises_value_error():
    with pytest.raises(ValueError):
        truncate("abc", -1)


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        truncate(123, 5)


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        truncate(None, 5)


def test_null_bytes_and_control_characters():
    assert truncate("\x00\x01\x02hello", 5) == "\x00\x01..."


def test_very_long_string():
    text = "a" * 1_000_000
    result = truncate(text, 100)
    assert result == "a" * 97 + "..."
    assert len(result) == 100
