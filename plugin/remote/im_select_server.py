#!/usr/bin/env python3
import socket
import subprocess

HOST = "::"
PORT = 12812

# 🔒 Whitelist of allowed input methods
IM_WHITELIST = {
    "com.apple.keylayout.ABC",
    "com.apple.keylayout.US",
    "com.apple.keylayout.Colemak",
    "com.apple.inputmethod.SCIM.ITABC",
    "",
    # add more as needed
}
error_str_prefix="E: Mac-input: "

def handle_client(conn):
    try:
        data = conn.recv(1024)
        msg = data.decode("utf-8").strip() if data else ""
        #print(msg)

        if msg in IM_WHITELIST:
            cmd_list=["im-select"]
            if msg:
                cmd_list.append(msg)
            try:
                result = subprocess.run(
                    cmd_list,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.DEVNULL,
                    text=True,
                    check=True
                )
                current_im = result.stdout.strip()
                if current_im == "":
                    current_im=msg
            except subprocess.CalledProcessError:
                current_im = error_str_prefix + "im_select failed"
        else:
            current_im = error_str_prefix + "invalid parameter"
        #print(current_im)
        conn.sendall((current_im + "\n").encode("utf-8"))

    finally:
        conn.close()

def main():

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"im-select server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()

