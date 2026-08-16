import unicodedata

_UMLAUT_TRANSLATIONS = {
    "ä": "ae",
    "ö": "oe",
    "ü": "ue",
    "Ä": "ae",
    "Ö": "oe",
    "Ü": "ue",
    "ß": "ss",
}


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    for umlaut, replacement in _UMLAUT_TRANSLATIONS.items():
        text = text.replace(umlaut, replacement)

    normalized = unicodedata.normalize("NFKD", text)
    decomposed = "".join(c for c in normalized if not unicodedata.combining(c))

    result: list[str] = []
    for char in decomposed.lower():
        if "a" <= char <= "z" or "0" <= char <= "9":
            result.append(char)
        elif result and result[-1] != "-":
            result.append("-")

    return "".join(result).strip("-")
