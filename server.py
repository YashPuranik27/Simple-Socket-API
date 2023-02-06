import threading
import time
import random
import socket
import client


def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # send an intro message to the client.
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    # server listens for a message from client.py
    ss.listen(400)
    print("[S]: Server is listening for a message from the client")

    # server reads a message sent by client.py
    clientData = csockid.recv(400)
    print("[S]: Data received from client: \n {}".format(clientData.decode('utf-8')))

    # reverses the message
    msg = clientData.decode('utf-8')
    msg = msg[::-1]
    msg = msg.splitlines()
    msg = msg[::-1]
    msg = '\n'.join(msg)

    # server sends the reversed message to client.py
    csockid.send(msg.encode('utf-8'))

    # server sends the reversed message to outr-proj.txt
    file = open("outr-proj.txt", "w")
    file.write(msg)
    file.close()

    # makes input upper case
    msg = clientData.decode('utf-8')
    msg = msg.upper()

    # server sends the upper case message to outup-proj.txt
    file = open("outup-proj.txt", "w")
    file.write(msg)
    file.close()

    # server sends the upper case message to client.py
    csockid.send(msg.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client.client)
    t2.start()
    time.sleep(5)
    print("Done.")
