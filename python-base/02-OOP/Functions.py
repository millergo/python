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


# 装饰器
def multiplier_single(func):
    # 闭包函数，内部函数可以访问外部函数局部作用域的变量
    def multiply_by_factor(number):
        # 这里可以做一些自己自定义的操作，比如对函数 factor 进行强加一些功能
        print("multiplier_single func:", func)
        return number * func

    # 返回的函数能够访问其定义所在的作用域。换而言之，它携带着自己所在的环境（和相关的局部变量）。
    # 也就是说 multiply_by_factor 现在携带了 multiplier_single 的数据。有点类似于Java的内部类。
    return multiply_by_factor


# 带参数的装饰器，factor为装饰器参数
def multiplier(factor):
    # func 接受被装饰的函数，相当于对目标函数进行处理，然后再返回目标函数
    def wrap(func):
        # 处理目标函数的参数
        def multiply_by_factor(*args, **kwargs):
            # 通常，不能给外部作用域内的变量赋值，但如果一定要这样做，可使用关键字nonlocal。
            # 这个关键字的用法与global很像，让你能够给外部作用域（非全局作用域）内的变量赋值.
            nonlocal factor
            factor += 1
            print("multiplier factor:", factor)
            # 处理完之后需要将目标函数返回
            return func(*args, **kwargs)

        return multiply_by_factor

    return wrap


# 使用带参数的装饰器。其实就是 multiplier = multiplier(2)
@multiplier(2)
def test_multiplier(number):
    number += 1
    print("test_multiplier：", number)


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
    # 调用 multiplier_single 函数时，实际上是不会执行 multiplier_single 内部的 multiply_by_factor 函数，而是返回 multiply_by_factor 函数
    # result = multiplier_single(2)
    # print(result)  # 这时候 result 相当于指向 multiply_by_factor 函数
    # print(result(5))  # 调用 multiply_by_factor 函数

    test_multiplier(888)
