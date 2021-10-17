#"Client to Client Chat Room"

import threading
import socket
host='127.0.0.1'
port =59000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))

server.listen()
clients=[]
Aliases=[]

def broadcast(message):
    for client in clients:
        client.send(message)

#Function to handle client connections
def handle_Client(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)

        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            alias=Aliases[index]
            broadcast(f'{alias} has left the chat room'.encode('utf-8'))
            Aliases.remove(alias)
            break

 # Main Function to receive the clients connection
def receive():

    while True:

        print("Server is running and waiting for connections")
        client,address=server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias=client.recv(1024)
        Aliases.append(alias)
        clients.append(client)
        print(f'The alias at this client is { alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        thread=threading.Thread(target=handle_Client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()



