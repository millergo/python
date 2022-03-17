class TestIterator:
    value = 0

    # 当你调用方法__next__时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，应引发StopIteration异常。
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    # 方法__iter__返回一个迭代器，它是包含方法__next__的对象，而调用这个方法时可不提任何参数。
    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))

g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print(4 ** 2)
result = sum(i ** 2 for i in range(3))
print(result)