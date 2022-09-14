import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
'''
try:
    client.sendto((b"DADOS", ("127.0.0.1", xxxx))
    print(client.recvfrom(1024))
except Exception as error:
    print("Erro de conexão")
    print(error)
'''

