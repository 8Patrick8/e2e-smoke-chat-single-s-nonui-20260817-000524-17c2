def ensure_str(text: str) -> str:
    """Prüft, dass ``text`` ein ``str`` ist, und gibt ihn unverändert zurück.

    Dies ist die einzige autoritative Definition der gemeinsamen
    Typ-Prüfungs-Konvention des Pakets: jede öffentliche Funktion lehnt
    Nicht-``str``-Eingaben mit ``TypeError`` ab.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return text
