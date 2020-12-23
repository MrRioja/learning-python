from socket import *

server = "127.0.0.1"
port = 12345

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)

print("Waiting for client...")

while True:
    con, client = obj_socket.accept()
    print("Connected with: ", client)
    while True:
        received_msg = str(con.recv(1024))
        print("We received: ", received_msg)
        sent_msg = b'Hello client'
        con.send(sent_msg)
        break
    con.close()
