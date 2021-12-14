import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 2), 6)
        self.assertNotEqual(add(4, 2), 5)

    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)
        self.assertNotEqual(subtract(4, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)
        self.assertNotEqual(multiply(4, 2), 10)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertNotEqual(divide(4, 2), 1)

unittest.main()