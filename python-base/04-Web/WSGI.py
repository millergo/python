"""
WSGI(Web Server Gateway Interface)
WSGI协议定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
可以把 WSGI 理解为 Java EE 标准，不同 WSGI服务器 都会它进行实现。比如Java中我们最早写的 Servlet API 就是一种JavaEE其中的一种技术标准协议，
不同的服务器都会此协议有相同的实现，所以我们写的代码能运行在不同的服务器（Tomcat、Jetty等）上，反而言之因为这些服务器都遵循了JavaEE的规范，
所以无论我们使用Spring MVC还是Struts2都可以正常运行在不同的服务器上，服务器负责将我们的数据处理完发送给客户端。我们开发应用程序时无需关注底层的
实现逻辑，由服务器帮助我们管理链接、资源等，但是其实底层都是Socket实现。
参考: https://peps.python.org/pep-0333/#environ-variables
"""


# application()函数由 WSGI服务器 来调用
def application(environ, start_response):
    """
    environ：一个包含所有HTTP请求信息的dict对象,通过这个对象我们可以拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header
    start_response：一个发送HTTP响应的函数。
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    method = environ['REQUEST_METHOD']
    print("请求方法为:", method)
    # 从environ里读取PATH_INFO
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # 返回响应体内容
    return [body.encode('utf-8')]
