import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))

with client:
    client.sendall(b'hello world\n')
    print(client.recv(1024).decode())
