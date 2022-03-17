"""
多态：
"""


# 类（class）的概念与Java中相同。
class Person:
    print("Person class invoked!")

    # setXxx,getXxx可以理解为Java中的普通JavaBean。
    def set_name(self, name):
        # self，关键字它指向对象本身。可以理解为Java中的this，表示当前对象。 self.name可以理解为向这个类中添加一个成员变量，名称叫做name。
        # 在Java中我们需要显示声明类的成员变量，而在Python中万物皆对象，所以可以直接通过 self.user_name 方式给对象添加属性。
        self.user_name = name

    def get_name(self):
        return self.user_name

    # 方法和函数的区别在于方法有个self参数，self会关联到它所属的实例
    def greet(self):
        print("Hello, world! I'm {}.".format(self.user_name))

    # 要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可.
    # 原理：在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头加上一个下划线和类名,比如 Person._Person__in_accessible(object)
    # 如果完全不希望外部访问name就用一个下划线
    def __in_accessible(self):
        print("我是私有方法，只能在类内部访问，外部不能直接访问")


if __name__ == "__main__":
    miller = Person()
    # 调用对象时会将miller对象作为第一个参数自动传递给self
    miller.set_name("Miller")
    miller.greet()

    mila = Person()
    mila.set_name("Mila")
    mila.greet()
    print("直接可以访问这些属性:", miller.user_name)
    # 访问私有属性或者方法的方法，不建议这么做
    Person._Person__in_accessible(miller)
