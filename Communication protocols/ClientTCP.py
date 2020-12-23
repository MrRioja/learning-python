from socket import *

server = "127.0.0.1"
port = 12345

msg = bytes(input("Type something: "), 'utf-8')

obj_socket = socket(AF_INET, SOCK_STREAM)

obj_socket.connect((server, port))
obj_socket.send(msg)

response = obj_socket.recv(1024)
print("We received: ", response)
obj_socket.close()
