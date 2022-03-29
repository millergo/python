from flask import Flask
from flask import make_response, redirect

app = Flask(__name__)


@app.route("/")
def index():
    # 第二个参数：返回的状态码；第三个参数：响应头字典
    return "<h1>Bad request</h1>", 400, {"header": "text/html", "Content-Type": "Miller test"}


@app.route("/response")
def response():
    response = make_response("<h1>使用make_response返回响应对象</h1>")
    response.set_cookie("name", "Miller")
    response.set_cookie("age", "32")
    response.status = 201
    response.calculate_content_length()
    return response


@app.route("/redirect")
def test_redirect():
    return redirect("http://www.baidu.com")


if __name__ == "__main__":
    app.run(debug=True)
