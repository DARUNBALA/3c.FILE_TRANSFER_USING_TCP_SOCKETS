import socket

HOST = socket.gethostname()
PORT = 60000
FILE = "mytext.txt"

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server listening...")
    while True:
        conn, addr = s.accept()
        print("Connected:", addr)

        msg = conn.recv(1024)    # <-- FIX: read client hello
        print("Client says:", msg.decode())
        FILE='D:\\SEM-2\\CN\\EX-3c\\3c.FILE_TRANSFER_USING_TCP_SOCKETS\\mytext.txt'
        with open(FILE, "rb") as f:
            for chunk in iter(lambda: f.read(1024), b""):
                conn.sendall(chunk)

        conn.shutdown(socket.SHUT_WR)   # tell client sending finished
        conn.close()
        print("File sent & connection closed")