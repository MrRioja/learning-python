import socket

resp = 'S'

while(resp == 'S'):
    url = input("Type the URL: ")
    ip = socket.gethostbyname(url)
    print("The IP for the informed URL is ", ip)
    resp = input("Type <S> to continue: ").upper()
