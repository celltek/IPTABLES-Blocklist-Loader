# IPTABLES Blocklist Loader

## Übersicht

Dieses Skript automatisiert das Herunterladen, Verarbeiten und Anwenden von Blocklisten für iptables. Es integriert IP-Adressen und Subnetze aus mehreren Quellen in die iptables-Regeln, um schädliche Verbindungen effektiv zu blockieren.

---

## Funktionen

- **Mehrere Blocklisten:** URLs können in einer Konfigurationsdatei definiert werden.
- **IP/Netzwerk-Validierung:** Nur gültige IPs/Subnetze werden verarbeitet.
- **Logging:** Aktivitäten und Fehler werden in einer Logdatei dokumentiert.
- **Flexibler Timeout:** Der Timeout-Wert für HTTP-Anfragen ist anpassbar.
- **Einfach konfigurierbar:** URLs werden aus einer JSON-Konfigurationsdatei geladen.

---

## Anforderungen

- Python 3.x
- Module: `requests`, `ipaddress`, `logging`, `subprocess`, `json`
- Zugriff auf `iptables`, `ip6tables`

---

## Installation

1. **Skript herunterladen:**
   ```bash
   git clone https://github.com/celltek/IPTABLES-Blocklist-Loader.git
   cd iptables_blocklist
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurationsdatei erstellen:**
   Erstelle eine `blocklist.json` im Hauptverzeichnis:
   ```json
   {
       "urls": [
           "https://example.com/blocklist.txt"
       ]
   }
   ```

---

## Nutzung

1. **Skript ausführen:**
   ```bash
   python3 blocklist.py
   ```

2. **Logdatei prüfen:**
   Alle Aktivitäten und Fehler werden in der Datei `blocklist.log` protokolliert.

---

## Warnhinweise

- Stelle sicher, dass du root-Berechtigungen hast, um `iptables`,`ip6tables`-Befehle auszuführen.
- Ungültige IP-Adressen/Subnetze werden automatisch übersprungen und im Log dokumentiert.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei `LICENSE`.

