"""
静态方法和类方法
"""


class MyClass:
    # 静态方法的定义中没有参数self，可直接通过类来调用。
    def smeth():
        print('This is a static method')

    smeth = staticmethod(smeth)

    # 类方法的定义中包含类似于self的参数，通常被命名为cls。对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。
    def cmeth(cls):
        print('This is a class method of', cls)

    cmeth = classmethod(cmeth)


if __name__ == "__main__":
    my_class = MyClass()
    my_class.smeth()
    my_class.cmeth()
    MyClass.smeth()
    MyClass.cmeth()
