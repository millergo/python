"""
字典: 字典由键及其相应的值组成，这种键值对称为项（ item）,是Python中的一种内置类型。字典中有很多类似于序列的操作，比如del, in, len等
Java: 作用于Java中的Map相同，存放键值对，key不可以重复、不可修改。
"""

from copy import deepcopy


def run():
    items = [('name', "Miller"), ('age', 30)]
    d = dict(items)
    print("使用 dict() 函数将 list 转换为 dict: ", d)  # {'name': 'Miller', 'age': 30}
    print("dict 取值:", d['name'])  # Miller

    d2 = dict(name="Miller", age=31)
    d2['age'] = 32
    print("使用dict()函数的关键字参数定义dict：", d2['age'])  # 32

    print("获取字典的长度：", len(d2))  # 2
    del d2['age']
    print("删除字典中的key和value：", d2)  # {'name': 'Miller'}
    print("检查字典d2是否包含键为k的项:", 'name' in d2)  # True

    person = {
        "Miller": {
            "email": "miller.shan@aliyun.com",
            "age": 30
        },
        "Mila": {
            "email": "mila@126.com",
            "age": 6
        }
    }
    print("获取键值：", person['Miller']['age'])

    # 像这样使用字典时，可指定任意数量的转换说明符，条件是所有的字段名都是包含在字典中的键。 比如替换HTML模板中的指定值，类似于Jinja模板
    print("当字符串中有些字符值与字典中的key相同时，可以使用字符串的 format_map() 方法进行格式化字符串。 \
            Miller's email is {Miller[email]}".format_map(person))


def test_clear_method():
    x = {}
    y = x
    x['name'] = 'Miller'
    print("y is :", y)
    # x = {}  # result:{'name': 'Miller'}
    x.clear()  # result:{}
    print("使用clear()方法清楚字典时，相关引用的也都会被全部清楚:", y)


# 浅拷贝, 当替换副本中的值时，原件不受影响。然而，如果修改副本中的值（就地修改而不是替换），原件也将发生变化
def test_copy_method():
    x = {"name": "Miller", "age": [30, 40]}
    y = x.copy()
    print("address is :", id(x['name']), id(y['name']))
    print("copy()之后的值 :", x, y)
    y["name"] = "Mila"  # 需要执行修改，而不是赋值,替换是不会影响原先的值,所以可以看到x的name值没有变化，但是age却因为y的修改改变了
    y["age"] = y["age"].pop()
    print("address is :", id(x['age']), id(y['age']))
    # y["age"].remove(40)
    # y["age"].remove(30)
    # y["age"].append(50)
    print("浅拷贝修改副本，原件值也被更新了,x = ", x)  # {'name': 'Miller', 'age': [50]}
    print("浅拷贝修改副本，副本值修改之后,y = ", y)  # {'name': 'Mila', 'age': [50]}
    # x 的修改影响 y
    # x["age"].append(60)
    # print("浅拷贝两个值修改 互相影响 对方", x, y)  # {'name': 'Miller', 'age': [50, 60]} {'name': 'Mila', 'age': [50, 60]}

    # 深拷贝,独立的两份，互相不受影响


def test_deep_copy_method():
    x = {"name": "Miller", "age": [30, 40]}
    y = deepcopy(x)
    y["name"] = "Mila"
    y["age"].remove(40)
    y["age"].remove(30)
    y["age"].append(50)
    print("深拷贝修改副本，原件值不被更新了,x = ", x)  # {'name': 'Miller', 'age': [30, 40]}
    print("深拷贝修改副本，副本值修改之后,y = ", y)  # {'name': 'Mila', 'age': [50]}
    # x 的修改不影响 y
    x["age"].append(60)
    print("深拷贝两个值修改 互相独立 不影响对方", x, y)  # {'name': 'Miller', 'age': [30, 40, 60]} {'name': 'Mila', 'age': [50]}


if __name__ == '__main__':
    # run()
    # test_clear_method()
    test_copy_method()
    print("-----------------------------------------\n")
    test_deep_copy_method()
