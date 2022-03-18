import socket

s = socket.socket()
# 获取当前机器的主机名
host = socket.gethostname()
port = 1234
s.bind((host, port))
# 方法listen接受一个参数——待办任务清单的长度（即最多可有多少个连接在队列中等待接纳，到达这个数量后将开始拒绝连接）。
s.listen(1)
while True:
    # 接受客户端连接,阻断（等待）到客户端连接到来为止，然后返回一个格式为(client, address)的元组
    c, addr = s.accept()
    print('Got connection from', addr)
    # 要发送数据，可调用方法send并提供一个字符串
    c.send(b'Thank you for connecting')
    c.close()
