import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('127.0.0.1',12345))
print("ready to send data")
while True:
    data,add=s.recvfrom(4087)
    print("message from Client: ")
    print(str(data))

    s_data=input("SERVER: ")
    message=bytes(s_data.encode('utf-8'))

    s.sendto(message,add)

    print("data has been sent from server")