"""
Python内置了WSGI服务器模块wsgiref,可以用于启动WSGI服务器，加载application()函数
"""
from wsgiref.simple_server import make_server
from WSGI import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 9001, application)
print("运行程序，浏览器输入 http://127.0.0.1:9001/Miller")
# 开始监听HTTP请求
httpd.serve_forever()
