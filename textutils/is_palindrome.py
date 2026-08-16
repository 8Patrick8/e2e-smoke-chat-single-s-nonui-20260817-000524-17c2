def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    cleaned = [ch for ch in text.lower() if ch.isalnum()]
    return cleaned == cleaned[::-1]
