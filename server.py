import socket

ADDRESS = '127.0.0.1'
PORT = 9999
MAX_WHOAMI_LENGTH = 16

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()

conn, addr = server.accept()

print(f"Connected: {addr}")

while True:
    print("checking")
    with conn:
        while data := conn.recv(1024):
            whoami = data[:MAX_WHOAMI_LENGTH]
            message = data[MAX_WHOAMI_LENGTH:]
            print(f"{whoami.decode()}")
            print(f"{message.decode()}")
