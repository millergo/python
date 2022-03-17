class Bird(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):

    def __init__(self):
        super().__init__()
        self.sound = "Squawk"

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    sb = SongBird()
    sb.sing()
    # 子类调用父类中的方法时，必须在子类初始化方法__init__中先调用父类的初始化方法super().__init__()
    sb.eat()
