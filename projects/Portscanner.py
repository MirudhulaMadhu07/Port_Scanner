import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        print(f"Port {port} is open")

print(f"Scanning {target}...")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan, range(start_port, end_port + 1))

print("Scan complete")