import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "time.nist.gov"
port = 13
s.connect((host,port))
while True:
    data = s.recv(10000)
    if data:
        print(data)
    else:
        break

s.close()