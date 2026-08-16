import textutils

PUBLIC_FUNCTIONS = [
    "slugify",
    "truncate",
    "word_count",
    "is_palindrome",
    "reverse_words",
]


def test_all_five_public_names_are_exported():
    for name in PUBLIC_FUNCTIONS:
        assert name in textutils.__all__


def test_all_five_public_names_are_callable():
    for name in PUBLIC_FUNCTIONS:
        assert callable(getattr(textutils, name))
