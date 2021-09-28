import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.81.1',1267))

print("connected to server")
while True:
# to read the data in client side
# 1024 buffer size   decoding as string format
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

    cdata=input("CLIENT:  ")
    s.send(bytes(cdata,'utf-8'))
    print("data has been sent to server")

