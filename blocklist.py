import requests
import ipaddress
import logging
import subprocess
import json

# Logging einrichten
def setup_logging():
    logging.basicConfig(
        filename="blocklist.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

# Blocklist herunterladen
def download_blocklist(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        logging.error(f"Fehler beim Herunterladen der Blockliste von {url}: {e}")
        return []

# Blockliste verarbeiten und validieren
def parse_blocklist(blocklist):
    ipv4_addresses = []
    ipv6_addresses = []
    
    for line in blocklist:
        line = line.strip()
        if not line or line.startswith("#"):  # Leere Zeilen und Kommentare ignorieren
            continue
        try:
            ip = ipaddress.ip_network(line, strict=False)
            if ip.version == 4:
                ipv4_addresses.append(str(ip))
            elif ip.version == 6:
                ipv6_addresses.append(str(ip))
        except ValueError:
            logging.warning(f"Ungültige IP/Subnetz gefunden und übersprungen: {line}")
    
    return ipv4_addresses, ipv6_addresses

# IPs zu Regeln hinzufügen
def add_ips_to_iptables(ipv4_list, ipv6_list):
    for ip in ipv4_list:
        try:
            subprocess.run(
                ["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"],
                check=True,
                capture_output=True,
            )
            logging.info(f"IPv4-Adresse/Subnetz erfolgreich hinzugefügt: {ip}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Fehler beim Hinzufügen von IPv4 {ip}: {e.stderr.decode()}")
    
    for ip in ipv6_list:
        try:
            subprocess.run(
                ["ip6tables", "-I", "INPUT", "-s", ip, "-j", "DROP"],
                check=True,
                capture_output=True,
            )
            logging.info(f"IPv6-Adresse/Subnetz erfolgreich hinzugefügt: {ip}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Fehler beim Hinzufügen von IPv6 {ip}: {e.stderr.decode()}")

# URLs aus Konfigurationsdatei laden
def load_urls_from_config(config_file="blocklist.json"):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            return config.get("urls", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Fehler beim Laden der Konfigurationsdatei: {e}")
        return []

# Hauptfunktion
def main():
    setup_logging()
    urls = load_urls_from_config()
    if not urls:
        logging.error("Keine gültigen URLs in der Konfigurationsdatei gefunden.")
        return

    timeout = 10  # Timeout für HTTP-Anfragen in Sekunden
    for url in urls:
        logging.info(f"Blockliste von {url} wird verarbeitet...")
        blocklist = download_blocklist(url, timeout)
        ipv4_list, ipv6_list = parse_blocklist(blocklist)
        add_ips_to_iptables(ipv4_list, ipv6_list)
        logging.info(f"Verarbeitung der Blockliste von {url} abgeschlossen.")

if __name__ == "__main__":
    main()
