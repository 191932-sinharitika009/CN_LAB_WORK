import socket

# socket for client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting with a server

s.connect(('192.168.81.1',2352))

msg=s.recv(1024)
print(msg.decode("utf-8"))