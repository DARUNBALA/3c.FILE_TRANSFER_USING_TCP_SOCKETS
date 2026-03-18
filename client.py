import socket

HOST = socket.gethostname()
PORT = 60000

with socket.socket() as s:
    s.connect((HOST, PORT))
    s.send(b"Hello server!")   # client hello

    with open("received.txt", "wb") as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)

print("File received successfully")