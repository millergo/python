"""
Flask-SQLAlchemy:专门针对flask框架开发一个操作数据库的框架
Java: hibernate，mybatis
"""
import json
import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置我们的应用需要链接的数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:autotest#123@192.168.9.43:3306/flask_dev?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化SQLAlchmy对象
db = SQLAlchemy(app)


# 定义数据模型，默认继承自db.Model
class Role(db.Model):
    # 数据库中的表名,如果不指定的话那么默认为类名称
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 一个角色可以属于多个用户。
    # relationship第一个参数表示建立的这种关系的模型是哪一个。而不会创建实际的字段，返回的是对象
    # backref参数向Role模型中添加一个role属性。
    # lazy参数表明加载相关记录的方式。比如select(首次访问时按需加载)， dynamic(不加载记录，但提供加载记录的查询)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # 把对象用字符串的形式表达出来
    def __repr__(self):
        return '<Role %r>' % self.name

    def to_json(self):
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # 外键约束，不建议使用. 每个用户都只能有一个角色。'roles.id'表示这个role_id的值是roles表中行的id值
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    # 将自定义对象转换为json，方式一
    # def to_json(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "role_id": self.role_id
    #     }

    # 将自定义对象转换为json，方式二
    def to_json(self):
        item = self.__dict__
        if "_sa_instance_state" in item:
            print(item["_sa_instance_state"])
            del item["_sa_instance_state"]
        return item


@app.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.filter_by(username="Miller").first()
    if user is None:
        user = User(username=random.randrange(1, 100, 1))
        db.session.add(user)
        # 提交修改
        db.session.commit()
        print(user)
    return user.to_json()


if __name__ == "__main__":
    # 根据模型自动创建表，如果表不存在的话.
    db.create_all()
    app.run(debug=True)
