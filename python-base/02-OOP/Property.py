"""
使用Property实现 getXxx, setXxx
"""


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    # 调用函数property并将存取方法作为参数（ 获取方法在前，设置方法在后）创建了一个特性，然后将名称size关联到这个特性
    size = property(get_size, set_size)


if __name__ == "__main__":
    r = Rectangle()
    r.width = 10
    r.height = 5
    print(r.size)
    print(r.get_size())
