import socket
import datetime

# creating a socket using a function socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket Created')
# binding the socket to port number  bind(ip,port no)
s.bind(('192.168.81.1',2352))

# No. clients you want to connect with
s.listen(3)
print("Waiting for connections")

# no of connections it want to accept
while True:
    c,addOfClient = s.accept()
    print(f"connected with {addOfClient}")
# Passing some message to client from server after connection

    c.send(bytes(str(datetime.datetime.now()),'utf-8'))

    c.close()