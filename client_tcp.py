import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.settimeout(5)
try:
    client.connect(("127.0.0.1", 4466))
    client.send(b"perdeu perdeu ahahaha\n")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Um erro ocorreu!!")