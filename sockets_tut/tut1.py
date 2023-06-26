from email import message
from encodings import utf_8
import socket

host = ""
port = 9999
s = socket.socket()
s.bind((host, port))
print("binding host and port", host, port)
s.listen(5)
conn, addr = s.accept()
print("coonection accepted", addr)

                
def send_command(conn):
    while True:
        choice = input("enter: ")
        mess = input("message: ")
        if choice == "quit":
            break
        tobesent = str.encode(mess)
        conn.send(tobesent)
        client_response = str(conn.recv(1024), "utf_8")
        print(client_response)
                
conn.close()
s.close()

