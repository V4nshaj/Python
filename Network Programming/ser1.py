import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '' 
port = 5555 
s.bind((host, port)) 
s.listen(5) 
while True: 
    c, addr = s.accept() #accepting the connection
    print('Got connection from', addr) 
    c.send(b'Thank you for connecting') 
c.close()
