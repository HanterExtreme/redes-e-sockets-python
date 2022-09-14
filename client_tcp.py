import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
client.settimeout(5)
try:
    client.connect(("127.0.0.1", xxxx))
    client.send(input(b"Mensagem: \n"))
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except Exception as error:
    print("Um erro ocorreu!!", error)
'''