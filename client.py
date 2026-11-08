import socket, sys

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9999

class NoNickPassedException(Exception):
    pass

try:
    whoami = sys.argv[1]
except IndexError:
    raise NoNickPassedException("Usage: python3 client.py <nick> max 99 chars")

MAX_WHOAMI_LENGTH = 16

nick_length = len(whoami)

if nick_length > 99:
    raise NoNickPassedException("Usage: python3 client.py <nick> max 99 chars")

if nick_length < 10:
    nick_length = f"0{nick_length}"
else:
    nick_length = str(nick_length)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))

with client:
    while(True):
        message = input("Message: ")
        output_message = nick_length + whoami + message
        message_bytes = output_message.encode()
        client.sendall(message_bytes)
