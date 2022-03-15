def run():
    x, y, z = 1, 2, 3
    print("序列解包:", x, y, z)  # 1, 2, 3

    values = 4, 5, 6
    x, y, z = values
    print("从对象中进行序列解包：", x, y, z)  # 4, 5, 6


def test_boolean():
    result = True + False + 3
    print("在Python中True的值为1， False为0：", result)  # 4
    # 标准值False和None、各种类型（包括浮点数、复数等）的数值0、空序列（如空字符串、空元组和空列表）以及空映射（如空字典）都被视为假，而其他各种值都被视为真
    print(bool(0))  # False
    print(bool(''))  # False
    print(bool(()))  # False
    print(bool([]))  # False
    print(bool({}))  # False
    print(bool(None))  # False


def test_if():
    name = "Miller.Shan"
    if name.endswith("Shan"):
        print("True")
    else:
        print("False")

    # 条件表达式 如果条件（紧跟在if后面）为真，表达式的结果为提供的第一个值（这里为"friend"），否则为第二个值（这里为"stranger"）。
    status = "friend" if name.endswith("er") else "stranger"  # stranger
    print(status)


# is 关键字比较是两个对象是否相同，而不是相等。类似于Java中的 instanceof。 == 符号比较的是对象的值。
def test_is():
    x = y = [1, 2, 3]
    z = [1, 2, 3]
    print(x == y)  # True
    print(x == z)  # True
    print(x is y)  # True
    print(x is z)  # False


def test_assert():
    age = 10;
    assert 0 < age < 100

    # age = 101;
    assert 0 < age < 100, "只有条件满足是下面的语句才会执行"
    print("assert test")


def test_loop_while():
    i = 0
    while i < 100:
        i += 1
    print("i is:", i, )  # 100


def test_loop_for():
    for number in range(1, 3):
        print(number)

    dic = {"x": 1, "y": 2, "z": 3}
    for key in dic:
        print("key is:", key, "value is ", dic[key])


def test_loop_zip():
    # 使用zip进行并行迭代
    names = ["Miller", "Mila", "Tom"]
    ages = [11, 10, 20]
    for name, age in zip(names, ages):
        print("name is :", name, " age is:", age)


def test_exec_method():
    exec("print('在字符串中执行Python代码')")


# 将字符串作为Python代码执行。有点Java中的反射的意思。
def test_eval_method():
    scope = {}
    scope["x"] = 2
    scope["y"] = 3
    result = eval("x * y", scope)
    print("result:", result)
    print(scope)


if __name__ == "__main__":
    # run()
    # test_boolean()
    # test_if()
    # test_is()
    # test_assert()
    # test_loop_while()
    # test_loop_for()
    # test_loop_zip()
    # test_exec_method();
    test_eval_method();
