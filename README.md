# textutils

Eine kleine, eigenständige Python-Bibliothek mit fünf unabhängigen
String-Hilfsfunktionen. Ohne UI, ohne Laufzeitabhängigkeiten außerhalb der
Standardbibliothek, mit Unit-Tests pro Funktion.

## Tech-Stack

- **Sprache**: Python (>= 3.9)
- **Packaging**: setuptools / `pyproject.toml`
- **Tests**: pytest

## Installation

```bash
pip install -e .
```

## Tests ausführen

```bash
pytest
```

## Verwendung

```python
from textutils import is_palindrome, reverse_words, slugify, truncate, word_count

slugify("Hello, World!")          # -> "hello-world"
truncate("Hallo Welt", 5)         # -> "Ha..."
word_count("  ein   Test  ")      # -> 2
is_palindrome("Hallo")            # -> False
reverse_words("eins zwei drei")   # -> "drei zwei eins"
```

## Öffentliche API

| Funktion | Signatur | Beschreibung |
| --- | --- | --- |
| `slugify` | `slugify(text: str) -> str` | Erzeugt einen URL-freundlichen Slug (nur `[a-z0-9-]`). |
| `truncate` | `truncate(text: str, max_len: int) -> str` | Kürzt Text mit `...`; wirft `ValueError` bei `max_len < 3`. |
| `word_count` | `word_count(text: str) -> int` | Zählt Wörter. |
| `is_palindrome` | `is_palindrome(text: str) -> bool` | Prüft auf Palindrom (ignoriert Satzzeichen und Leerzeichen). |
| `reverse_words` | `reverse_words(text: str) -> str` | Kehrt die Wortreihenfolge um. |

Alle fünf Funktionen prüfen zuerst `isinstance(text, str)` und werfen sonst `TypeError`.

## Feature-Liste

- Fünf unabhängige String-Hilfsfunktionen als flaches Paket `textutils`.
- Einheitliche Typprüfung (`TypeError` bei Nicht-`str`-Eingabe).
- Keine Datei- oder Netzwerkzugriffe; keine Aufrufe von `eval`, `exec`, `subprocess` oder `os.system`.
