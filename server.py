import socket
import os
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ThreadCount = 0
try:
    s.bind((socket.gethostname(), 1233))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
s.listen(3)


def threaded_client(connection):
    # connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        print('Server received', data.decode("utf-8"))
        filename = 'mytext.txt'
        f = open(filename, 'rb')
        l = f.read(1024)

        while (l):
            connection.send(l)
            print("sent ", repr(l))
            l = f.read(1024)
        f.close

        print("done sending file")
        # connection.send(bytes("thank you for connecting", "utf-8"))
        connection.close


while True:
    Client, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
s.close()
