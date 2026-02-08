#!/usr/bin/env python3
import socket
import subprocess

HOST = "0.0.0.0"
PORT = 12812

# 🔒 Whitelist of allowed input methods
IM_WHITELIST = {
    "com.apple.keylayout.ABC",
    "com.apple.keylayout.US",
    "com.apple.keylayout.Colemak",
    "com.apple.inputmethod.SCIM.ITABC",
    # add more as needed
}

def handle_client(conn):
    try:
        data = conn.recv(1024)
        msg = data.decode("utf-8").strip() if data else ""

        if msg:
            if msg in IM_WHITELIST:
                subprocess.run(
                    ["im-select", msg],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False
                )
            # else: silently ignore invalid parameter
        else:
            # Query current input method
            result = subprocess.run(
                ["im-select"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False
            )
            current_im = result.stdout.strip()
            if current_im:
                conn.sendall((current_im + "\n").encode("utf-8"))
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"im-select server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()

