import socket
from datetime import datetime


def port_scanner():
    target = input("Enter IP address or domain: ")

    print("-" * 50)
    print(f"scanning target: {target}")
    print(f"time started: {datetime.now()}")
    print(f"-" * 50)

    try:
        for port in range(1, 1025):
            # Creating a socket (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port))
            if result == 0:
                print(f"port {port}: OPEN")

            s.close()
    # error listing
    except Exception as e:
        print(f"\nError detected: {e}")


if __name__ == "__main__":
    port_scanner()
