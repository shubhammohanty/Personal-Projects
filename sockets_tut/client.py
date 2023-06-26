import socket
import threading

HOST = ""
PORT = 9090

clientend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
clientend.connect((HOST, PORT))
print("Connected to server")

n = input("Enter your name: ")
clientend.send(n.encode())

def send(clientend):
    while True:
        msg = input("enter your message: \n")
        print(" ")
        clientend.send(msg.encode())

def receive(clientend):
    while True:
        recd = clientend.recv(1024).decode()
        print(recd)
  
t1 = threading.Thread(target=send, args=(clientend,))
t1.start()
t2 = threading.Thread(target=receive, args=(clientend,))
t2.start()
