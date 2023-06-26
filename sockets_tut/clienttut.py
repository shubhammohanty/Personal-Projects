import socket

host = "192.168.1.3"
port = 2222
s = socket.socket()
s.connect((host, port))
print("connected to server")

while True:

    data = str(s.recv(1024), "utf8")
    print("received data from server is ", data)
    s.send(str.encode("return"))

    