#Server
import socket
s=socket.socket()
print('Socket Created')

host=socket.gethostname()
port=9999

s.bind((host,port))
s.listen(3)
print('waiting for the client connection')

while True:
    c,addr=s.accept()
    print(s.recv(1024).decode())
    print('connected with',addr)
    c.send(bytes('welcome','utf-8'))
    s.close()