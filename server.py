import socket
host = '127.0.0.1'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("waiting for connect")
while 1:
    conn,addr = s.accept()
    print("connected by", addr)
    data = conn.recv(1024)
    print(data)
    conn.close()
s.close()

