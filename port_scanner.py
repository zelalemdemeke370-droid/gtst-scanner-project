import socket
import sys
from datetime import datetime

target = input("Please enter the Host IP/Domain you want to scan: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[!] Hostname could not be resolved. Please verify the input.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target Host: {target_ip}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

ports = [21, 22, 23, 25, 53, 80, 443]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()

except KeyboardInterrupt:
    print("\n[-] Scan cancelled by user.")
    sys.exit()
except socket.error:
    print("\n[!] Could not connect to the server.")
    sys.exit()