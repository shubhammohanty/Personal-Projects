import socket
import threading

HOST = ""
PORT = 9090
clients = []
names = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print("server binded")
server.listen()
print("server listening...")
 
def broadcast(message):
    for conn in clients:
        conn.send(message)

def rxtx(conn):
    while True:
        try:
            x = conn.recv(1024)
            print(x)
            broadcast(x)
        except:
            ind = clients.index(conn)
            clients.remove(conn)
            nameitem = names[ind]
            names.remove(nameitem)
            conn.close()
            print(nameitem, "removed")
            print(clients)

def receive():
    while True:
        conn, address = server.accept()
        nickname = conn.recv(1024)

        clients.append(conn)
        names.append(nickname)
        print(clients)
        print(nickname, "with address ", address, "is connected to the server")

        thread1 = threading.Thread(target=rxtx, args=(conn,))
        thread1.start()

receive()