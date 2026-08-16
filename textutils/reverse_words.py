from textutils._validation import ensure_str


def reverse_words(text: str) -> str:
    """Kehrt die Reihenfolge der durch Whitespace getrennten Wörter um."""
    ensure_str(text)

    return " ".join(reversed(text.split()))
