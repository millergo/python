"""
实现自定义的序列
"""


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    # __getitem__(self, key)：这个方法应返回与指定键相关联的值。对序列来说，键应该是0~n-1的整数，其中n为序列的长度。对映射来说，键可以是任何类型
    def __getitem__(self, index):
        # 添加一个计数的功能.每当你访问列表元素时，这个属性的值都加1。
        print("访问元素时 __getitem__ method invoked")
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

    #  __setitem__(self, key, value)：这个方法应以与键相关联的方式存储值，以便以后能够使用__getitem__来获取。当然，仅当对象可变时才需要实现这个方法
    def __setitem__(self, key, value):
        print("修改元素时 __setitem__ method invoked")


if __name__ == "__main__":
    my_list = CounterList(range(10))
    print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list.counter)  # 0
    # 每次访问元素时__getitem__方法就会被调用，这里应为访问了2次，所以结果应该为2
    my_list[4] + my_list[2]
    print(my_list.counter)  # 2
    # 调用方法则不会触发__getitem__方法执行
    my_list.remove(5)
    print(my_list)  # [0, 1, 2, 3, 4, 6, 7, 8, 9]
    print(my_list.counter)  # 2
    # 修改元素时会触发 __setitem__ 方法的调用
    my_list[5] = 11
    print(my_list.counter)  # 2
