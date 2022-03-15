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


if __name__ == "__main__":
    # test_keyword_parameters("Miller")  # Hello Miller!
    # test_keyword_parameters("Miller", "Good Morning")  # Good Morning Miller!
    # test_keyword_parameters("Miller", "Good Morning", "-,-")  # Good Morning Miller -,-
    # test_keyword_parameters("Miller", punctuation="-,-")  # Hello Miller -,-
    # test_keyword_parameters("Miller", greeting="Good Night")  # Good Night, Miller!

    # test_params("Miller", 30)  # ('Miller', 30) Node
    # test_params("Miller", 30, last_param_must_keyword="miller.shan@aliyun.com")  # ('Miller', 30) miller.shan@aliyun.com
    # test_multi_keyword_params(name="Miller", age=30, address="HangZhou")
    test_args_and_keyword("Hello ", "Miller, Mila, Vicky", age1=30, age2=20,  )
