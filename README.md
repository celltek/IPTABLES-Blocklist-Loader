# Fail2ban Blocklist Loader

## Übersicht

Dieses Skript automatisiert das Herunterladen, Verarbeiten und Anwenden von Blocklisten für Fail2ban. Es integriert IP-Adressen und Subnetze aus mehreren Quellen in die iptables-Regeln, um schädliche Verbindungen effektiv zu blockieren.

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
- Zugriff auf `iptables`

---

## Installation

1. **Skript herunterladen:**
   ```bash
   git clone <repository-url>
   cd fail2ban_blocklist
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurationsdatei erstellen:**
   Erstelle eine `blocklist_config.json` im Hauptverzeichnis:
   ```json
   {
       "urls": [
           "https://ipv64.net/blocklists/ipv64_blocklist_spamhaus_drop.txt",
           "https://example.com/blocklist.txt"
       ]
   }
   ```

---

## Nutzung

1. **Skript ausführen:**
   ```bash
   python fail2ban_blocklist.py
   ```

2. **Logdatei prüfen:**
   Alle Aktivitäten und Fehler werden in der Datei `fail2ban_blocklist.log` protokolliert.

---

## Warnhinweise

- Stelle sicher, dass du root-Berechtigungen hast, um `iptables`-Befehle auszuführen.
- Ungültige IP-Adressen/Subnetze werden automatisch übersprungen und im Log dokumentiert.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei `LICENSE`.

