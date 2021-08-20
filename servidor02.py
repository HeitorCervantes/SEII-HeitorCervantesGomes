import socket
import sys
from thread import *
 
host = ''
port = 1234
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
try:
    s.bind((host, port))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
      
s.listen(1)
 
def clientthread(conn):

   while True:


	namefile = conn.recv(1024).decode()

	with open(namefile, 'rb') as file:
		for data in file.readlines():
			conn.send(data)

		print('Arquivo enviado!')


while True:
 
    conn, addr = s.accept()
    
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    start_new_thread(clientthread ,(conn,))
