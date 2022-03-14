"""
Python 数据结构：序列 \
几乎在所有情况下都可使用列表来代替元组。一种例外情况是将元组用作字典键, 在这种情况下，不能使用列表来代替元组，因为字典键是不允许修改的. \
序列感觉有点像Python中特有的概念，在Java中我们一般是使用数组或者集合来做索引的操作。
- 通用序列操作：索引、 切片、 相加、 相乘和成员资格
"""


def test_sequence():
    person_miller = ["Miller", 30]
    person_mila = ["mila", 6]
    database = [person_miller, person_mila]
    print(database[0])
    print(database[0][0])
    
    # 字符串就是由字符组成的序列
    literal = 'Miller'
    print(literal[0])
    print(literal[-1])

    # 切片
    slicing = "Miller"
    print("切片操作：" + slicing[0:3])

    # 第一个索引是包含的第一个元素的编号，但第二个索引是切片后余下的第一个元素的编号。
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("多次切片：", numbers[0:9][4])
    print("从末尾开始往前切片：", numbers[-4:-2])
    print("如果切片结束于序列末尾，可省略第二个索引：", numbers[-4:])
    print("如果切片开始于序列开头，可省略第一个索引：", numbers[:4])
    print("复制整个序列，可将两个索引都省略：", numbers[:])
    print("使用步长切出奇数：", numbers[0:9:2])
    # 为负数，即从右向左提取元素
    print("使用步长切出偶数：", numbers[9:0:-2])

    print("序列相加进行拼接:", [1, 2, 3] + [4, 5, 6])

    # 在Python中， None表示什么都没有，可以理解为Java中的 null
    sequence = None
    print("None value:", sequence)


# 检查特定的值是否包含在序列中，可使用运算符in
def test_check_value():
    name = "Miller"
    print("e" in name)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(13 in numbers)


# 列表,可将任何序列（而不仅仅是字符串）作为 list 的参数
def test_list():
    name = "Miller"
    to_list = list(name)
    print("将字符串转换为列表: ", to_list)  # ['M', 'i', 'l', 'l', 'e', 'r']
    to_string = '-abc '.join(to_list)
    print("将列表转换为字符串: ", to_string)  # M-abc i-abc l-abc l-abc e-abc r

    alphabet = ['a', 'b', 'c', 1, 2, 3]
    alphabet[0] = 'z'
    alphabet[4] = 'f'
    print("使用索引修改列表:", alphabet)  # ['z', 'b', 'c', 1, 'f', 3]

    del alphabet[2]
    print("删除列表:", alphabet)  # ['z', 'b', 1, 'f', 3]

    print("对列表进行切片:", alphabet[0:2])  # ['z', 'b']
    name = list('Puppy')
    name[1:] = list('ython')
    print("对列表进行切片:", "".join(name))  # Python
    name.append("Java")
    name.append("y")
    print("向列表追加对象:", name)  # ['P', 'y', 't', 'h', 'o', 'n', ' Java']

    print("计算指定的元素在列表中出现了多少次:", name.count('y'))  # 2
    temp = ['t', 'e', 's', 't']

    # 返回的是一个新的对象
    name.extend(temp)
    print("将对象附加到列表末尾:", name)  # ['P', 'y', 't', 'h', 'o', 'n', 'Java', 'y', 't', 'e', 's', 't']

    name.clear()
    print("清空列表:", name)  # []

    new_name = ["Miller", "Jerry", "Mila", "Vicky", "Mila", "Tom", "Mila"]
    print("在列表中查找指定值第一次出现的索引:", new_name.index("Mila"))  # 2

    new_name.insert(3, "Dog")
    print("将一个对象插入列表:", new_name)  # ['Miller', 'Jerry', 'Mila', 'Dog', 'Vicky', 'Mila', 'Tom', 'Mila']

    # 使用pop可实现一种常见的数据结构——栈（ stack）,后进先出（ LIFO）。
    new_name.append("Wow")
    print(type(new_name))
    new_name = new_name.pop()
    print("从列表中删除一个元素（末尾为最后一个元素），并返回这一元素:", new_name)  # Wow

    scope = [20, 30, 60, 30, 70, 80, 20]
    scope.remove(30)
    print("删除第一个为指定值的元素:", scope)  # [20, 60, 30, 70, 80, 20]

    scope.reverse()
    print("按相反的顺序排列列表中的元素:", scope)  # [20, 80, 70, 30, 60, 20]

    scope.sort()
    print("对列表就地排序:", scope)  # [20, 20, 30, 60, 70, 80]

    print("对列表就地排序,并返回列表:", sorted(scope))  # [20, 20, 30, 60, 70, 80]


# 元组，不可修改的序列。类似于Java中的final。
def test_tuples():
    t = 1,
    print("元组必须有逗号：", t)  # (1,)
    t = ()
    print("也可以使用()定义元组：", t)  # ()

    t2 = 3 * (2 + 2,)
    print(t2)  # (4, 4, 4)

    # 函数tuple的工作原理与list很像：它将一个序列作为参数，并将其转换为元组
    t3 = tuple([1, 2, 3])
    print("使用tuple()函数定义元组：", t3)  # (1, 2, 3)

    print(tuple('abc'))  # ('a', 'b', 'c')


if __name__ == '__main__':
    test_sequence()
    # test_check_value()
    # test_list()

    # test_tuples()
