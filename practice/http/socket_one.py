import socket

# Create a socket
# AF_INET specifies IPv4
# SOCK_STREAM specifies TCP protocol
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))       # Connect to the server's port 80

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()    # HTTP Request
mysock.send(cmd)    # Send the request

while True:
    data = mysock.recv(512)     # Read upto 512 bytes at once from OS's TCP Buffer

    if len(data) < 1: break     # If no more data left, break

    print(data.decode(), end=" ")

mysock.close()