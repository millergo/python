# Python 中的模块
import math
# 每次调用函数时可不用指定模块名
from math import sqrt


def fun():
    # 调佣math模块的函数sqrt，计算平方根
    result = math.sqrt(9)
    print(result)
    # 调用函数时可不用指定模块名
    result = sqrt(9)
    print(result)

    # 使用变量来引用函数,因为是变量指向引用，所以不需要括号。此时foo指向sqrt函数
    foo = math.sqrt
    print(foo(9), foo)


if __name__ == '__main__':
    fun()
