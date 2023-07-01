#Server
import socket
s=socket.socket()
print('Socket Created')

host=socket.gethostname()#gethostname
port=9999#port number

s.bind((host,port))
s.listen(3)#wait for 3 seeconds
print('waiting for the client connection')

while True:
    c,addr=s.accept()#accept the connection
    print(s.recv(1024).decode())
    print('connected with',addr)
    c.send(bytes('welcome','utf-8'))
    s.close()
