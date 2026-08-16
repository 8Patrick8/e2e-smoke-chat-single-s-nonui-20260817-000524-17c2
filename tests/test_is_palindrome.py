import pytest

from textutils.is_palindrome import is_palindrome


def test_sentence_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("Ein Neger mit Gazelle zagt im Regen nie") is True


def test_non_palindrome_returns_false():
    assert is_palindrome("Hallo") is False


def test_empty_string_is_palindrome():
    assert is_palindrome("") is True


def test_single_character_is_palindrome():
    assert is_palindrome("a") is True


def test_single_digit_is_palindrome():
    assert is_palindrome("7") is True


def test_case_insensitive_palindrome():
    assert is_palindrome("Anna") is True


def test_mixed_case_palindrome():
    assert is_palindrome("RaceCar") is True


def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_digit_palindrome():
    assert is_palindrome("12321") is True


def test_digit_non_palindrome():
    assert is_palindrome("12345") is False


def test_unicode_palindrome_ignores_punctuation():
    assert is_palindrome("Rüben, Rüben?") is False


def test_unicode_letters_handled():
    assert is_palindrome("äööä") is True
    assert is_palindrome("äöüä") is False


def test_palindrome_with_null_bytes():
    assert is_palindrome("a\x00b\x00a") is True


def test_palindrome_with_control_characters():
    assert is_palindrome("\n\tA b a\r") is True


def test_very_long_palindromic_string():
    text = "a" * 1_000_000
    assert is_palindrome(text) is True


def test_very_long_non_palindromic_string():
    text = ("a" * 500_000) + "b"
    assert is_palindrome(text) is False


def test_only_non_alphanumeric_returns_true():
    assert is_palindrome("!!! ...") is True


def test_non_string_raises_type_error():
    for value in (None, 42, 3.14, ["a"], {"a": 1}, b"abc"):
        with pytest.raises(TypeError):
            is_palindrome(value)
