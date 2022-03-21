"""
Python内置了 WSGI服务器 模块wsgiref,可以用于启动 WSGI服务器 ，加载application()函数，但是这个模块只是做了一个最简单的实现，所以项目中一般不用。
可以将 WSGI服务器 理解为Java中的Tomcat，因为我们编写的代码都需跑某个 WSGI服务器 上，WSGI服务器 实现了WSGI标准，从而实现对HTTP资源的各种操作。
"""
from wsgiref.simple_server import make_server
from WSGI import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 9001, application)
print("运行程序，浏览器输入 http://127.0.0.1:9001/Miller")
# 开始监听HTTP请求
httpd.serve_forever()
