import nmap

# Initialize the Nmap PortScanner object
nm = nmap.PortScanner()

target = input("Please enter the target IP: ")
print("\n[+] Nmap scan in progress, please wait...")

# Run a TCP scan on ports 21 through 80
nm.scan(target, '21-80', '-v')

# Iterate through all discovered hosts
for host in nm.all_hosts():
    print("-" * 40)
    print(f"Host : {host} ({nm[host].hostname()})")
    print(f"State : {nm[host].state()}") # Shows if the host is 'up' or 'down'
    
    for protocol in nm[host].all_protocols():
        print(f"Protocol : {protocol}")
        
        lport = nm[host][protocol].keys()
        for port in sorted(lport):
            state = nm[host][protocol][port]['state']
            name = nm[host][protocol][port]['name']
            print(f"Port : {port}\tState : {state}\tService : {name}")