import socket
import sys
from datetime import datetime

def basic_scanner(target):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        # Scanning ports 1 to 100 for demonstration
        for port in range(1, 101):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1) # Short timeout for faster scanning
            
            result = sock.connect_ex((target, port))
            
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            sock.close()

    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()

    print("-" * 50)
    print("Scanning Completed.")

# Run the scanner on localhost
if __name__ == "__main__":
    target_ip = "127.0.0.1" 
    basic_scanner(target_ip)
    