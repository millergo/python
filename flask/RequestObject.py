"""
- Flask收到客户端的请求之后，会自动创建一个请求对象（request），并且将请求对象临时在Flask上下文中设置为全局，这样每个视图函数都可以访问，
而不需要在每个视图函数的参数中定义 request 对象，保持方法的声明干净。每个视图函数独立持有 request 对象，以保证多线程时的安全性。
Flask有两种上下文：程序上下文、请求上下文。变量如下
| 变量名 | 上下文 | 作用域 |
| ---- | ---- | ---- |
| current_app | 程序上下文 | 当前活动程序的实例 |
| g           | 程序上下文 | 处理请求时用作临时存储的对象。每次请求都会重设这个变量 |
| request     | 请求上下文 | 请求对象，封装了客户端发送请求的HTTP请求中的所有内容 |
| session     | 请求上下文 | 用户会话，存储请求之间值的一个字典 |

- Java: 在Java中我们是用过在方法参数中添加 HttpServletRequest 对象来获取客户端的请求对象。
"""
from flask import Flask
from flask import request
from flask import current_app

app = Flask(__name__)


# Flask中的视图函数(路由)，客户端访问Flask时的请求URL。类似于Java中的@RequestMapping()
@app.route("/")
def index():
    print(id(request))
    response = "请求上下文 request:" + str(id(request)) \
               + "请求方法：" + request.method \
               + "</br>程序上下文 current_app: " + current_app.name \
               + "<br/> 当前请求的路由：" + str(current_app.url_map)
    print("request:{}, method:{}, current_app.name:{}, current_app.url_map:{}".format(id(request), request.method,
                                                                                      current_app.name,
                                                                                      current_app.url_map))

    return response


if __name__ == "__main__":
    app.run(debug=True)
