from textutils._validation import ensure_str


def truncate(text: str, max_len: int) -> str:
    """Kürzt ``text`` auf höchstens ``max_len`` Zeichen und hängt bei Bedarf ``...`` an.

    Wirft ``ValueError`` bei ``max_len < 3``.
    """
    ensure_str(text)
    if max_len < 3:
        raise ValueError("max_len must be at least 3")
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."
