#!/usr/bin/env python3
import socket
import sys
import os

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

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((mac_host, PORT))
        s.sendall((im_id + "\n").encode("utf-8"))

        if not im_id:
            data = s.recv(1024)
            if data:
                print(data.decode("utf-8").strip())

if __name__ == "__main__":
    main()

