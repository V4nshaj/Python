#Client
import socket

c=socket.socket()
host=socket.gethostname()
port=9999
c.connect((host,port))
name=input("Enter your name: ")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())
c.close()