import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))

s2 = socket.socket()
s2.connect((host, port))

s3 = socket.socket()
s3.connect((host, port))
# 要接收数据，可调用recv并指定最多接收多少个字节的数据
print(s.recv(1024))
print(s2.recv(1024))
print(s3.recv(1024))
