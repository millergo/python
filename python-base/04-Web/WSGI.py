"""
WSGI(Web Server Gateway Interface)
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
"""


# application()函数必须由WSGI服务器来调用
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
