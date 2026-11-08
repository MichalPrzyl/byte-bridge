import socket, sys

whoami = sys.argv[1]
MAX_WHOAMI_LENGTH = 16

if len(whoami) <= 0:
    raise ValueError("set whoami")

elif len(whoami) > MAX_WHOAMI_LENGTH:
    whoami = whoami[:MAX_WHOAMI_LENGTH]

elif len(whoami) < MAX_WHOAMI_LENGTH:
    whoami = whoami + ('0' * (MAX_WHOAMI_LENGTH - len(whoami)))


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))

with client:
    while(True):
        message = input("Message: ")
        abc = whoami + message
        message_bytes = abc.encode()
        client.sendall(message_bytes)
