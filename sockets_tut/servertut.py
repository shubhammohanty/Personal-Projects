from re import S
import socket

host = "192.168.1.3"
port = 2222
def create_socket():
    global s
    try:
        s = socket.socket()
        print("socket successfully created")
    
    except socket.error as msg:
        print("socket creation error", str(msg))


def bind_socket():
    try:
        global host
        global port
        s.bind((host, port))
        print("socket successfully binded to ",host,"at", port, " server is waiting for connection")
        s.listen(5)
    
    except socket.error as msg1:
        print("socket binding error", str(msg1), "Retrying...")
        bind_socket

def socket_accept():
    global conn
    conn, addr = s.accept()
    print(addr)

def send_receive(conn):
    while True:
        choice = input("enter your choice(quit to quit): ")
        if choice == "quit":
            break
        messg = input("enter your message you want to send: ")
        messg = str.encode(messg)
        conn.send(messg)
        client_response = str(conn.recv(1024), "utf8")
        print("received data from client is ",client_response)


def main():
    create_socket()
    bind_socket()
    socket_accept()
    send_receive(conn)
    conn.close()
    s.close()

main()

