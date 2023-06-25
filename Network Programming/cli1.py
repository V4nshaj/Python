import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = 'server ip address..' 
port = 5555 
try: s.bind((host, port)) 
except socket.error as e: print(str(e)) 
s.connect((host, port)) 
print(s.recv(1024)) 
s.close()