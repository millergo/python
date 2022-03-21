import unittest, math


class ProductTestCase(unittest.TestCase):
    @staticmethod
    def test_integers():
        math.pow(2, 3)

    @staticmethod
    def test_floats():
        math.sqrt(4)


if __name__ == "__main__":
    unittest.main()
