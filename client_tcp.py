# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
<<<<<<< HEAD
server_address = ('142.251.41.78',80)
=======
server_address = ('10.20.61.14', 10000)
>>>>>>> c189f034f81e211eb508d3fa3436067e95158ff8
print('Connexion TCP a %s sur le port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
<<<<<<< HEAD
    message = 'GET / HTTP/1.0'
=======
    #message = 'GET / HTTP/1.0\r\n Host: google.com\r\n\r\n'
    message = 'allumer_LED'
>>>>>>> c189f034f81e211eb508d3fa3436067e95158ff8
    print('Envoi de : "%s"' % message)
    sock.sendall(message.encode())
    


finally:
    print('Fermeture du socket TCP')
    sock.close()