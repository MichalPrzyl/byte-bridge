import socket

ADDRESS = '127.0.0.1'
PORT = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()

conn, addr = server.accept()

print(f"Connected: {addr}")

with conn:
    while data := conn.recv(1024):
        print(data.decode())
        conn.sendall(data)
