import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("connection is created")
c.bind(('192.168.81.1',1267))

# To make the server socket listen to the client request

c.listen()

print("server is waiting for connection")

# connection object and address of the client is returned
conn,add = c.accept()
print("Connected to client")

while True:
# Sending data to client ,utf-8(data format)
    data=input("SERVER:  ")
    conn.send(bytes(data,'utf-8'))
    print("Data has been sent")

# Receiving from client
    recData = conn.recv(1024)
    print("Data from client",recData.decode())


c.close()