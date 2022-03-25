"""

继承：继承父类的所有属性和方法
如果多个父类中有同名的方法，会就近开始寻找，寻找父类中的重写的方法，前面的覆盖后面的
"""


class Animal:
    def run(self):
        print("Animal can be run")

    def sleep(self):
        print("Animal can be sleep")


# 语法：class 类名(父类名称)
class Dog(Animal):
    def bark(self):
        print("Dog can be Go Go Go")

    def run(self, a):
        print("Dog override run")


class HaShiqi(Dog):
    def ha(self):
        print('HaShiQi...')


h = HaShiqi()
h.run(1)  # Dog override run
# 子类中没有去父类中中，父类中有，然后发现参数不匹配
# h.run()  # TypeError: run() missing 1 required positional argument: 'a'
h.sleep()  # Animal can be sleep
h.bark()  # Dog can be Go Go Go
h.ha()  # HaShiQi...


# 多重继承
class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test(self):
        print('BBB')


# 多重继承
class C(A, B):
    pass


# 打印C的所有父类
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)

r = C()
#  如果多个父类中有同名的方法，会就近开始寻找，寻找父类中的重写的方法，前面的覆盖后面的
r.test()  # AAA
