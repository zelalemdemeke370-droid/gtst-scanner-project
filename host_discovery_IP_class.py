import os
import socket
import struct

def get_gateway_ip():
    """Retrieves the Default Gateway IP from system routing tables (Optimized for Linux)"""
    try:
        with open("/proc/net/route") as fh:
            for line in fh:
                fields = line.strip().split()
                if fields[1] == '00000000': # Identifies the Default Gateway mask in Linux
                    return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
    except Exception:
        return "Could not determine Gateway (This feature works natively on Linux)"
    return "Gateway not found"

def determine_ip_class(ip):
    """Categorizes the IPv4 address into its respective Class architecture"""
    try:
        first_octet = int(ip.split('.')[0])
        if 1 <= first_octet <= 126:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "Class E (Experimental)"
        else:
            return "Invalid IP Range (Loopback or Out-of-bounds)"
    except ValueError:
        return "Invalid IP address formatting"

# Execution block
gateway = get_gateway_ip()
print(f"[+] Your Default Gateway IP: {gateway}")

user_ip = input("\nEnter an IP address to classify: ")
ip_class = determine_ip_class(user_ip)
print(f"[+] The IP Class for {user_ip} is: {ip_class}")