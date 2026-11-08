import socket

ADDRESS = '127.0.0.1'
PORT = 9999
MAX_WHOAMI_LENGTH = 16

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ADDRESS, PORT))
server.listen()

while True:
    conn, addr = server.accept()

    print(f"Connected: {addr}")

    with conn:
        while data := conn.recv(1024):
            nick_length = int(data[:2].decode())
            nick = data[2:2+nick_length]
            message = data[nick_length+2:]
            print(100*'-')
            print(f"{nick.decode()}")
            print(f"{message.decode()}")
