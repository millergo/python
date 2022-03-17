"""
递归：每次调用函数时，都将为此创建一个新的命名空间。这意味着函数调用自身时，是两个不同的函数［更准确地说，是不同版本（即命名空间不同）的同一个函数］在交流。
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(3))
