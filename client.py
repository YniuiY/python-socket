import socket
host = '127.0.0.1'
port = 50007
name = "yang di"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = input('>')
s.send(data.encode())
s.close()