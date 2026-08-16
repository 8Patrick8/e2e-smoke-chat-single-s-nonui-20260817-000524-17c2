from textutils._validation import ensure_str


def is_palindrome(text: str) -> bool:
    """Prüft, ob ``text`` ein Palindrom ist.

    Groß-/Kleinschreibung, Satzzeichen und Leerzeichen werden ignoriert.
    """
    ensure_str(text)

    cleaned = [ch for ch in text.lower() if ch.isalnum()]
    return cleaned == cleaned[::-1]
