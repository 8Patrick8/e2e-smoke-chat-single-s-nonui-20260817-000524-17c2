def word_count(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    return len(text.split())
