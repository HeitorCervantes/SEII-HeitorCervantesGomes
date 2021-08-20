import socket
import sys

host = 'localhost'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

namefile = str(input('Arquivo:'))

s.send(namefilme.encode())

with open(namefile, 'wb') as file:
	while 1:
		data = s.recv(1000000)
		if not data: break
		file.write(data)

print(f'{namefile} recebido!\n')
