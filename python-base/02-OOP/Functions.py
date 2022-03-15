"""
函数
"""


# 关键字参数，使用参数名称来指定参数的默认值
def test_keyword_parameters(name, greeting="Hello", punctuation="!"):
    print('{}, {}{}'.format(greeting, name, punctuation))


# 任意数量的位置参数。类似于Java中的可变参数，其实是一个数组
def test_params(*args, last_param_must_keyword=None):
    print(args, last_param_must_keyword)


# 接收多个关键字参数，然后自己在方法内部处理接收的关键字参数
def test_multi_keyword_params(**kwargs):
    print("接收多个关键字参数:", kwargs)


# 组合使用位置参数和关键字参数
def test_args_and_keyword(first_arg, *args, **kwargs):
    print("接收多个位置参数、关键字参数:", first_arg, args, kwargs)


def test_scope():
    x = 1
    # vars的内置函数，它返回这个不可见的字典
    scope = vars()
    print(scope["x"])
    scope["x"] += 1
    print(scope["x"])


# 使用global访问全局变量
def test_scope2(parameter):
    print(parameter + globals()["external"])


# 全局变量
external = " Hello"


def multiplier(factor):
    def multiply_by_factor(number):
        print(factor)
        return number * factor

    print(factor)
    return multiply_by_factor  # 返回里面的函数


if __name__ == "__main__":
    # test_keyword_parameters("Miller")  # Hello Miller!
    # test_keyword_parameters("Miller", "Good Morning")  # Good Morning Miller!
    # test_keyword_parameters("Miller", "Good Morning", "-,-")  # Good Morning Miller -,-
    # test_keyword_parameters("Miller", punctuation="-,-")  # Hello Miller -,-
    # test_keyword_parameters("Miller", greeting="Good Night")  # Good Night, Miller!

    # test_params("Miller", 30)  # ('Miller', 30) Node
    # test_params("Miller", 30, last_param_must_keyword="miller.shan@aliyun.com")  # ('Miller', 30) miller.shan@aliyun.com
    # test_multi_keyword_params(name="Miller", age=30, address="HangZhou")
    # test_args_and_keyword("Hello ", "Miller, Mila, Vicky", age1=30, age2=20)
    # test_scope()
    # test_scope2("Miller")
    # 调用 multiplier 函数时，实际上是不会执行 multipliter 内部的 multiply_by_factor 函数，而是返回 multiply_by_factor 函数
    result = multiplier(2)
    print(result)  # 这时候 result 相当于指向 multiply_by_factor 函数
    print(result(5))  # 调用 multiply_by_factor 函数
