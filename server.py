import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '00.00.00.00'
port = 444

serversocket.bind(('00.00.00.00', port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print('Connetion established from %s' % str(address))
    
    message = "Thank you for connecting to the server" + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
