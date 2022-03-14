# Python 中的模块，可以理解为将一个文件内容导入到当前文件内容中。
import math
# 每次调用函数时可不用指定模块名。这种写法有些类似于Java中的类 import static 导入类操作，\
# 不同的是在Java中只有通过静态导入的类才可以直接写方法名，而非非静态的如果直接调用方法需要先 new ObjectPerson();
from math import sqrt


def fun():
    # 调佣math模块的函数sqrt，计算平方根
    result = math.sqrt(9)
    print(result)
    # 调用函数时可不用指定模块名
    result = sqrt(9)
    print(result)

    # 使用变量来引用函数,因为是讲引用赋值给变量，所以不需要括号。此时foo指向sqrt函数。与Java中相同，可以理解为把引用赋值给一个新的引用
    foo = math.sqrt
    print(foo(9), foo)


if __name__ == '__main__':
    fun()
