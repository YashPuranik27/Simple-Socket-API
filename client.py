import threading
import socket


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Receive data from the server
    serverData = cs.recv(400)
    print("[C]: Data received from server: {}".format(serverData.decode('utf-8')))

    # client reads a file named in-proj.txt and sends it to the server
    file = open("in-proj.txt", "r")
    msg = file.read()
    cs.sendall(msg.encode())

    # client receives the message from server.py and prints it
    serverData = cs.recv(400)
    print("[C]: Data received from server: \n {}".format(serverData.decode('utf-8')))
    serverData = cs.recv(400)
    print("[C]: Data received from server: \n {}".format(serverData.decode('utf-8')))
    # close the client socket
    cs.close()
    exit()

# main function for client.py


def startup():
    t2 = threading.Thread(name='client', target=client)
    t2.start()
