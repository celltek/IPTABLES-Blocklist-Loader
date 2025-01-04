# Dokumentation: IPTABLES Blocklist Loader

## Einleitung

Der IPTABLES Blocklist Loader ist ein Python-Skript, das automatisch Blocklisten von angegebenen URLs herunterlädt und diese in die iptables-Regeln integriert, um schädliche IP-Adressen und Subnetze zu blockieren. Dieses Dokument beschreibt die Funktionsweise, Konfiguration und Nutzung des Skripts.

---

## Aufbau des Skripts

### Module und Funktionen

1. **setup_logging**
   - Konfiguriert die Logdatei (`blocklist.log`) und das Logging-Format.
   
2. **download_blocklist**
   - Lädt Blocklisten von angegebenen URLs herunter. Verwendet einen konfigurierbaren Timeout-Wert.

3. **parse_blocklist**
   - Validiert und filtert gültige IP-Adressen und Subnetze aus der heruntergeladenen Blockliste.

4. **add_ips_to_iptables**
   - Fügt die validierten IPs/Subnetze zu den iptables-Regeln hinzu.

5. **process_blocklist**
   - Koordiniert das Herunterladen, Verarbeiten und Anwenden einer einzelnen Blockliste.

6. **load_urls_from_config**
   - Liest die URLs der Blocklisten aus einer JSON-Konfigurationsdatei.

7. **main**
   - Hauptfunktion, die den Workflow steuert und alle Blocklisten verarbeitet.

---

## Konfigurationsdatei

Die Blocklisten-URLs werden in einer Datei namens `blocklist.json` definiert. Beispiel:

```json
{
    "urls": [
        "https://example.com/blocklist.txt"
    ]
}
```

- **`urls`**: Liste der Blocklisten-URLs.

---

## Nutzung

### Voraussetzungen
- Python 3.x
- Root-Berechtigungen für `iptables`, `ip6tables`
- Installierte Python-Module: `requests`, `ipaddress`, `logging`, `json`

### Ausführen des Skripts

1. **Skript starten:**
   ```bash
   python3 blocklist.py
   ```

2. **Logs überprüfen:**
   Das Skript protokolliert alle Aktivitäten in `blocklist.log`.

### Fehlerbehebung
- **Fehler beim Herunterladen:**
  - Prüfe die URL in der `blocklist.json`.
  - Stelle sicher, dass der Server erreichbar ist.

- **Fehler bei iptables-Befehlen:**
  - Stelle sicher, dass das Skript mit root-Berechtigungen ausgeführt wird.
  - Prüfe vorhandene iptables-Regeln auf Konflikte.

---

## Logdatei

Die Logdatei `blocklist.log` enthält:
- Erfolge und Fehler beim Herunterladen der Blocklisten.
- Details zu ungültigen Einträgen.
- Status der hinzugefügten IP-Adressen/Subnetze.

Beispiel:
```
2025-01-04 10:15:00 - INFO - Blockliste von https://example.com/blocklist.txt erfolgreich heruntergeladen.
2025-01-04 10:15:01 - INFO - IP/Subnetz erfolgreich hinzugefügt: 192.168.0.0/24
2025-01-04 10:15:02 - WARNING - Ungültige IP oder Subnetz gefunden und übersprungen: invalid_entry
```

---

## Erweiterungen

- **Timeout konfigurierbar:** Der Timeout-Wert für HTTP-Anfragen kann angepasst werden.
- **Mehrere Blocklisten:** Das Skript verarbeitet beliebig viele URLs.
---

## Lizenz

Das Projekt steht unter der GPL-3.0-Lizenz. Details sind in der Datei `LICENSE` zu finden.

