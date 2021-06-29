import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Waiting for connection')
s.connect((socket.gethostname(), 1233))


s.send(bytes("hello server", "utf-8"))

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print(data)

        if not data:
            break
        # write data to a file
        f.write(data)

    f.close()

print('Successfully got the file')
s.close()
print('connection closed')
