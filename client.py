#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '00.00.00.00'
port = 444

clientsocket.connect(('00.00.00.00', port)) 

message = clientsocket.recv(1024)

clientsocket.close()
print(message.decode('ascii'))
