#!/usr/bin/env python3
import socket
import sys
import os
from ipaddress import ip_address, IPv4Address, IPv6Address

PORT = 12812

def get_mac_host():
    ssh_conn = os.environ.get("SSH_CONNECTION")
    if not ssh_conn:
        raise RuntimeError("SSH_CONNECTION not set (not in SSH session)")

    # Format: client_ip client_port server_ip server_port
    return ssh_conn.split()[0]

def main():
    im_id = sys.argv[1] if len(sys.argv) == 2 else ""

    mac_host = get_mac_host()

    if type(ip_address(mac_host)) is IPv4Address:
        socket_family=socket.AF_INET
    elif type(ip_address(mac_host)) is IPv6Address:
        socket_family=socket.AF_INET6
    else:
        print("error unknown address")
        return

    with socket.socket(socket_family, socket.SOCK_STREAM) as s:
        s.connect((mac_host, PORT))
        s.sendall((im_id + "\n").encode("utf-8"))

        if not im_id:
            data = s.recv(1024)
            if data:
                print(data.decode("utf-8").strip())

if __name__ == "__main__":
    main()

