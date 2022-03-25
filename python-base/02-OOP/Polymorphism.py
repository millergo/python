"""
多态:python中的多态主要是通过对象的属性来实现的，只要对象中含有"name"属性，它就可以作为参数传递，而并不会考虑对象的类型
"""


# 多态：其实就是看属性或者方法，有就可以调用，没有则不行
class A:
    def __init__(self, name):
        # 使用双下划线定义隐藏属性,这样类的外部就没法直接访问，因为Python解析器会自动给双下划线属性自动重新命名为_A.__name
        self.__name = name

    # 使用装饰器@property来装饰方法为getter方法。注意：方法名称必须与属性名一致
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class B:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class C:
    pass


# 定义一个方法接受一个对象，然后获取对象的name属性
def say_hello(obj):
    print('Hello:%s' % obj.name)


def say_hello2(obj):
    # 检查类型
    if isinstance(obj, A) or isinstance(obj, B):
        print('Hello:%s' % obj.name)
    else:
        print('不支持的类型:%s' % type(obj))


# 创建对象
object1 = A("Hi")
# 给对象设置属性，相当于调用set_name方法
object1.name = 'Tom'
# 获取属性值，相当于调用get_name方法
# print(object1.name)

# 调用方法，传递对象1
say_hello(object1)  # Hello:Tom
object2 = B("Jerry")
# 调用方法，传递对象2
say_hello(object2)  # Hello:Jerry
# 调用方法，传递对象3
object3 = C()
# say_hello(object3)  # AttributeError: 'C' object has no attribute 'name'
'''
    多态总结：对于def say_hello(obj):这个函数来说，只要对象中含有name属性，它就可以作为参数传递
                这个函数并不会考虑对象的类型，只要有name属性即可
'''
print('======================================>')
say_hello2(object1)  # Hello:Tom
say_hello2(object2)  # Hello:Jerry
say_hello2(object3)  # 不支持的类型:<class '__main__.C'>
