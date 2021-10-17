import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    c_data=input("CLIENT: ")
    message = bytes(c_data.encode('utf-8'))
    c.sendto(message, ('127.0.0.1', 12345))
    data, addr = c.recvfrom(4087)

    print("message from Server: ")
    print(str(data))