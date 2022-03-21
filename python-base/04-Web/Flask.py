"""
Flask是一个应用程序框架，它也实现了WSGI接口，让我们能更加轻松的编写我们的业务逻辑，而不需要关注WSGI协议。
可以将Flask理解为Java中的Servlet、SpringMVC框架
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def powers(n=10):
    return ','.join(str(2 ** i) for i in range(n))


@app.route("/powers/<int:n>")
def powers_2(n=10):
    return ','.join(str(2 ** i) for i in range(n))


if __name__ == "__main__":
    app.run()
