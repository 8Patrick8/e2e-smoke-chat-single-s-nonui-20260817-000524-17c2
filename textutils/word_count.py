from textutils._validation import ensure_str


def word_count(text: str) -> int:
    """Zählt die durch Whitespace getrennten Wörter in ``text``."""
    ensure_str(text)

    return len(text.split())
