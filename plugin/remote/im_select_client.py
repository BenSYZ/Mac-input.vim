#!/usr/bin/env python3
import socket
import sys
import os
from ipaddress import ip_address, IPv4Address, IPv6Address

PORT = 12812
error_str_prefix="E: Mac-input: "
def get_mac_host():
    ssh_conn = os.environ.get("SSH_CONNECTION")
    if not ssh_conn:
        raise RuntimeError("SSH_CONNECTION not set (not in SSH session)")

    # Format: client_ip client_port server_ip server_port
    return ssh_conn.split()[0]

def main():
    im_id = ""
    timeout=0.5
    if len(sys.argv) == 2:
        im_id = sys.argv[1]
    elif len(sys.argv) == 3:
        im_id = sys.argv[1]
        timeout = float(sys.argv[2])

    mac_host = get_mac_host()

    if type(ip_address(mac_host)) is IPv4Address:
        socket_family=socket.AF_INET
    elif type(ip_address(mac_host)) is IPv6Address:
        socket_family=socket.AF_INET6
    else:
        print("error unknown address")
        return

    with socket.socket(socket_family, socket.SOCK_STREAM) as s:
        #print(timeout)
        s.settimeout(timeout)
        #print(mac_host)
        try:
            s.connect((mac_host, PORT))
            s.sendall((im_id + "\n").encode("utf-8"))
            data = s.recv(1024)
            result = data.decode("utf-8").strip()
        except (ConnectionRefusedError, TimeoutError) as _:
            result = error_str_prefix + "Timeout"

        print(result)
        if result.startswith(error_str_prefix):
            return 1

if __name__ == "__main__":
    sys.exit(main())

