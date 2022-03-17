"""
构造函数.
在Python中， 有些名称很特别，开头和结尾都是两个下划线。
如果你的对象实现了这些方法，它们将在特定情况下（具体是哪种情况取决于方法的名称）被Python调用，而几乎不需要直接调用
"""


class Person:
    # 可以把 __init__ 方法理解为Java中的构造方法，当我们创建一个对象Object()并且写了()号时会像Java一样由解释器自动调用
    def __init__(self, name):
        self.name = name
        print("__init__方法被Python解释器自动调用了")

    # 析构函数（ destructor）。这个方法在对象被销毁（作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使用__del__。
    def __del__(self):
        print("什么时候才能执行我啊。。。")


if __name__ == "__main__":
    p1 = Person
    # 可以把 () 理解为调用构造方法
    p1 = Person("Miller")
    print(p1.name)
