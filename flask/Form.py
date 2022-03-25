"""
处理请求中的表单
"""
import requests
from flask import Flask, render_template, session, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        flash("请求了 GET 方法")
    elif request.method == "POST":
        flash("请求了 POST 方法")
    else:
        flash("请求方法未处理" + request.method)
        return redirect(url_for("http://www.baidu.com"))
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
