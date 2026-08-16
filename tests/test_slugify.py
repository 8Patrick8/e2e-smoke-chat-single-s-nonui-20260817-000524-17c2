from textutils.slugify import slugify

_ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789-")


def test_slugify_ac01_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_ac02_umlauts():
    assert slugify("Grüße aus München!") == "gruesse-aus-muenchen"


def test_slugify_lowercase():
    assert slugify("HELLO WORLD") == "hello-world"


def test_slugify_umlaut_mapping():
    assert slugify("ä ö ü ß") == "ae-oe-ue-ss"


def test_slugify_uppercase_umlauts():
    assert slugify("ÄÖÜ") == "aeoeue"


def test_slugify_special_characters_become_dashes():
    assert slugify("foo!bar?baz") == "foo-bar-baz"


def test_slugify_path_separators_become_dashes():
    assert slugify("foo/bar\\baz") == "foo-bar-baz"


def test_slugify_collapses_repeated_dashes():
    assert slugify("a---b") == "a-b"


def test_slugify_strips_leading_and_trailing_dashes():
    assert slugify("-hello-") == "hello"
    assert slugify("!!!hello!!!") == "hello"


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_whitespace_only():
    assert slugify("   ") == ""


def test_slugify_keeps_digits():
    assert slugify("Version 2.0") == "version-2-0"


def test_slugify_accented_latin_is_decomposed():
    assert slugify("café") == "cafe"


def test_slugify_null_bytes_never_remain():
    assert "\x00" not in slugify("a\x00b\x00c")
    assert slugify("a\x00b") == "a-b"


def test_slugify_control_characters_never_remain():
    assert slugify("a\x01\x02b\x03") == "a-b"


def test_slugify_ac13_output_only_allowed_chars():
    result = slugify("Héllo\r\nWörld\t\x07/\x00\\")
    assert set(result) <= _ALLOWED
    assert "/" not in result
    assert "\\" not in result
    assert "\x00" not in result


def test_slugify_very_long_string_over_one_million_chars():
    text = "Grüße " * 200_000 + "x"
    assert len(text) > 1_000_000
    result = slugify(text)
    assert set(result) <= _ALLOWED
    assert result == "gruesse-" * 200_000 + "x"


def test_slugify_million_plus_characters_single_word():
    assert slugify("a" * 1_000_001) == "a" * 1_000_001


def test_slugify_non_str_raises_typeerror():
    for bad_input in (None, 42, 3.14, ["Hello"], b"Hello", {"a": 1}):
        try:
            slugify(bad_input)  # type: ignore[arg-type]
        except TypeError:
            pass
        else:
            raise AssertionError(f"slugify({bad_input!r}) should raise TypeError")
