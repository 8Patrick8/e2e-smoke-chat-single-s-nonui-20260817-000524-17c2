VERDICT: CHANGES_REQUESTED

## Prüfrahmen

Geprüfter Stand: reine Python-Bibliothek `textutils` (Backend, ohne UI, ohne Datei-/Netzwerkzugriffe). Einschlägige Rechtsbereiche: DSGVO und EU Cyber Resilience Act (CRA). Nicht einschlägig: EU AI Act (keine KI-Funktion vorhanden), Impressum/Terms/Privacy/Cookie-Pflichten und WCAG/BITV/EAA-Barrierefreiheit (keine öffentliche Web-UI).

---

## 1. DSGVO / Datenschutz

**Befund:** Der Produktcode verarbeitet Eingaben ausschließlich flüchtig im Arbeitsspeicher. Es gibt keine Dateizugriffe, keine Netzwerkkommunikation, kein Logging, keine Persistenz. Daher entstehen keine gespeicherten personenbezogenen Daten, keine Protokolle mit personenbezogenen Inhalten und keine Übermittlung an Dritte. Ein Verstoß gegen die DSGVO ist auf Codeebene nicht erkennbar. Die datenschutzrechtliche Verantwortung für die übergebenen Zeichenketten liegt beim jeweiligen Anwender.

**Findings:**

- **[low] Datenfluss nicht dokumentiert.**  
  Es fehlt eine klare Aussage, dass die Bibliothek keine Daten speichert, loggt oder überträgt. Für datenschutzkonforme Nachnutzung sollte das explizit dokumentiert sein.  
  **Remedy:** In `README.md` einen Abschnitt `Sicherheit & Datenschutz` ergänzen, z. B.:  
  „Alle Funktionen verarbeiten Eingaben ausschließlich flüchtig im Arbeitsspeicher. Es erfolgt keine Speicherung, Protokollierung, Datei- oder Netzwerkübertragung. Personenbezogene Daten bleiben in der Verantwortung des Aufrufers.“

- **[low] Potenziell diskriminierender Beispieltext in Tests und Anforderung.**  
  Der sichtbare Test `tests/test_is_palindrome.py` sowie AC-08 der Sprint-Spec verwenden den veralteten und rassistisch konnotierten Begriff „Neger“. Das ist kein DSGVO-Verstoß, aber ein rechtlich-reputatives und gleichbehandlungsrechtlich relevantes Risiko.  
  **Remedy:** In `tests/test_is_palindrome.py` in `test_sentence_palindrome_ignores_case_and_punctuation` den String ersetzen durch ein neutrales Satzpalindrom, z. B. `assert is_palindrome("Ein Esel lese nie.") is True`. AC-08 der Sprint-Spec analog anpassen.

---

## 2. EU Cyber Resilience Act (CRA)

**Befund:** Sicherheitskritische Aufrufe (`eval`, `exec`, `subprocess`, `os.system`, Datei-/Netzwerkzugriffe) sind im Produktcode nicht vorhanden. `slugify` beschränkt die Ausgabe auf `[a-z0-9-]`; Pfadtrenner, Null-Bytes und Steuerzeichen verbleiben nicht im Slug. Die Tests decken sehr lange Eingaben und Fehlerfälle ab. Insgesamt sind die technischen Sicherheitsanforderungen für diese kleine Bibliothek solide umgesetzt.

**Findings:**

- **[medium] SBOM / maschinenlesbares Abhängigkeitsverzeichnis fehlt.**  
  Es gibt keine sichtbare SBOM-Datei (z. B. CycloneDX/SPDX). Die Abhängigkeiten sind nur implizit in `pyproject.toml` enthalten.  
  **Remedy:** Neue Datei `sbom.json` (CycloneDX 1.5) im Repository ergänzen. Darin mindestens aufführen: `textutils` 0.1.0, Python `>=3.9`, Build-Abhängigkeit `setuptools`, optionale Dev-Abhängigkeit `pytest`. Alternativ kann ein SBOM-Generator in die CI aufgenommen werden, der die SBOM bei Releases automatisch erzeugt.

- **[medium] Security-Policy / dokumentierte Sicherheitseigenschaften fehlen.**  
  Es ist keine sichtbare `SECURITY.md` oder vergleichbare Dokumentation zu Meldeweg, unterstützten Versionen und Patch-Verhalten vorhanden.  
  **Remedy:** Neue Datei `SECURITY.md` anlegen mit mindestens: Sicherheitskontakt bzw. Meldeweg, unterstützte Versionen, Umgang mit gemeldeten Schwachstellen und Bestätigung, dass der Produktcode keine `eval`/`exec`/`subprocess`/`os.system`-Aufrufe und keine Datei- oder Netzwerkzugriffe enthält. In `README.md` auf diese Datei verweisen.

- **[low] Build-Abhängigkeit ohne obere Versionsgrenze.**  
  `pyproject.toml` fordert `setuptools>=68` ohne Obergrenze, was die Reproduzierbarkeit und das Änderungsmanagement erschwert.  
  **Remedy:** In `pyproject.toml` eine obere Grenze ergänzen, z. B. `requires = ["setuptools>=68,<76"]`. Die Dev-Abhängigkeit `pytest>=8.0,<9.0` ist bereits korrekt begrenzt. Optional zusätzlich einen Lockfile-Mechanismus für reproduzierbare Builds einführen.

---

## 3. EU AI Act

Nicht anwendbar: Die Bibliothek enthält keine KI-Funktion, kein maschinelles Lernen und keine automatisierte Entscheidungsfindung.

---

## 4. Pflichttexte & UI / Accessibility

Nicht anwendbar: Reine Backend-Bibliothek ohne öffentliche Web-UI, ohne Cookies, ohne Tracking und ohne Endnutzer-Oberfläche. Es bestehen daher keine Impressums-, Datenschutzerklärungs-, Cookie-Consent- oder WCAG/BITV/EAA-Pflichten für dieses Produkt selbst.

---

## Gesamtergebnis

Kein fundamentaler Rechtsverstoß erkennbar, daher nicht `BLOCKED`. Vor einer Marktfreigabe sind jedoch die CRA-Dokumentationslücken (SBOM, Security-Policy, Abhängigkeitsbegrenzung) zu schließen und der diskriminierende Beispieltext in Tests und Anforderung zu ersetzen.