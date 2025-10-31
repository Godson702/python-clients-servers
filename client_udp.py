# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
server_address = ('google.com', 80)
print('Envoi UDP a %s sur le port %s' % server_address)
message = 'bmw m5.'
print('Envoi : "%s"' % message)
sock.sendto(message.encode(), server_address)
    
# Look for the response
amount_received = 0
amount_expected = len(message)
data = sock.recvfrom(amount_expected)
amount_received += len(data)
print('Recu :  "%s"' % data[0].decode())
