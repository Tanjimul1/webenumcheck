import requests
import socket
from bs4 import BeautifulSoup
import threading

def website_enumeration(target):
 print("[+] Starting website enumeration on:", target)
    
subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail']
    for subdomain in subdomains:
        url = f"http://{subdomain}.{target}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found Subdomain: {url}")
        except requests.ConnectionError:
            pass

try:
        ip = socket.gethostbyname(target)
        print(f"[+] IP address of {target}: {ip}")
        for port in [80, 443, 8080, 8443]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open on {target}")
            sock.close()
    except socket.error as e:
        print(f"[!] Error: {e}")
