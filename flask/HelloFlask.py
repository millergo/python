from flask import Flask

# __name__ 程序的主模块或者包的名字
app = Flask(__name__)


# Flask中的视图函数(路由)，客户端访问Flask时的请求URL。类似于Java中的@RequestMapping()
@app.route("/")
def index():
    return "<h1>Hello Flask</h1>"


if __name__ == "__main__":
    # debug=True每次修改保存自动重启服务器，一般用于本地开发环境
    app.run(debug=True)
