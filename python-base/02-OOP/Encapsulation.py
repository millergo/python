"""
封装
总结：
    实例属性：没法通过类访问，只能通过实例访问
    类属性  ：可以通过类访问，可以通过实例访问
    类方法  ：可以通过类访问，可以通过实例访问
    实例方法：可以通过类访问，可以通过实例访问
    静态方法：可以通过类访问，可以通过实例访问
"""


# 类的定义
class Person:
    # 注意：定义在类中的属性是不能被类中的方法访问的。但是是可以通过对象访问的,p.my_name='Miller'，或者通过类访问Person.my_name.
    # 如果要访问类中的属性，那么需要通过@classmethod来访问
    my_name = 'default_value'

    # 类的特殊方法（魔术方法），每次在类实例化时都会自动调用。
    # 作用：用于初始化对象的属性
    def __init__(self, arg):
        # print('访问类中的属性:', my_name)  # NameError: name 'my_name' is not defined
        # 通过self代表当前对象。 向对象中添加一个属性__name，双下划线定义的属性，外部不能访问，只能在类内部访问.
        # 但是实际上只是把名称改成了“_类名__属性名”，其实还是可以访问的，是个假隐藏属性
        self.__name = arg

    # 注意：在类中定义方法时，默认调用时会传递一个参数，所以方法中至少要有一个形参。一般叫self，当然你可以起个名字叫this
    # 方法中不能直接访问类的属性
    def say_hello(this):
        print("Hello:%s" % this.__name)

    def get_name(self):
        return self.__name

    # 定义一个实例方法，第一个参数为self
    def set_name(self, name):
        self.__name = name
        return self.__name

    #   类方法，第一个参数为cls
    @classmethod
    def get_class_property(cls):
        print('我是类方法，我可以访问类的属性: ', cls.my_name)

    #  静态方法，可以不用指定参数
    @staticmethod
    def invoke_static_method():
        print("我是静态方法,其实就是一个函数，与当前类无关，只是放到当前类中来管理")


# 创建对象
p1 = Person('Miller');
p2 = Person('Jack');
# 调用对象中的方法时，默认python解析器会传递一个实参给方法

print(p1.my_name, type(p1))  # default_value <class '__main__.Person'>
print(p2.my_name, type(p2))  # default_value <class '__main__.Person'>
'''
方法与函数的区别：
    1. 方法是通过 对象.方法名()调用的
    2. 方法调用时默认会传递一个参数，所以方法中至少要定义一个形参
'''

p1.say_hello()  # Hello:Miller
p2.say_hello()  # Hello:Jack

"""
总结：创建对象的流程
1. 声明一个变量。
2. 在内存中开辟内存空间，存储对象的数据。
3. 调用魔术方法“__init__"
4. 返回对象的地址（Id）存储到变量中。

"""
p1.set_name("p1-name")
r = p1.get_name()
print('r=', r)  # r= p1-name
p1.say_hello()  # Hello:p1-name

p2.set_name("p2=name")
r_p2 = p2.get_name()
print('r_p2', r_p2)  # r_p2 p2=name
p2.say_hello()  # Hello:p2=name

print('==============调用类方法=================')
# 可以通过类去调用
Person.get_class_property()
# 可以通过实例调用
p2.get_class_property()
print('==============调用静态方法=================')
Person.invoke_static_method();
p2.invoke_static_method()
