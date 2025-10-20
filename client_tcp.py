# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('142.251.41.78', 80)
print('Connexion TCP a %s sur le port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'GET / HTTP/1.0\r\n Host: google.com\r\n\r\n'
    print('Envoi de : "%s"' % message)
    sock.sendall(message.encode())
    
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('Recu :  "%s"' % data.decode())

finally:
    print('Fermeture du socket TCP')
    sock.close()