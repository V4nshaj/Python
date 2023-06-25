import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "time.nist.gov"
port = 13
s.bind((host,port))
while True:
    c,addr=s.accept()
    data = time.ctime()
    if data:
        print(data)
        s.send(data.encode())
    else:
        break

s.close()