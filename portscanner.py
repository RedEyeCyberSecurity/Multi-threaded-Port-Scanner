import socket
import threading


# Function to scan a single port
def scan_target(ip, port):
    try:
        # Attempt to connect to the given IP and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout
            s.connect((ip, port))
            print(f"[+] Found open port {port}")
    except:
        pass


# Function to start scanning with threading
def scan_ports(ip, ports):
    print(f"Scanning IP: {ip}")
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_target, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Main execution
if __name__ == "__main__":
    target_ip = input("Enter the target IP: ")
    port_range = range(1, 1025)  # Example: Scan ports 1 to 1024
    scan_ports(target_ip, port_range)
