import unittest
from output import print_calcul
from operation_functionality import add, subtract, multiply, divide

class TestCalcul(unittest.TestCase):

    def test_addition(self):
        total = 1
        print_calcul(total, add, [1, 2, 3], "+", "addition")
        self.assertTrue(total, 6)

    def test_soustraction(self):
        total = 1
        print_calcul(total, subtract, [1, 2, 3], "-", "soustraction")
        self.assertTrue(total, -4)

    def test_multiply(self):
        total = 1
        print_calcul(total, multiply, [1, 2, 3], "*", "multiplication")
        self.assertTrue(total, 6)

    def test_divide(self):
        total = 1
        print_calcul(total, divide, [1, 2], "/", "division")
        self.assertTrue(total, 1/2)

if __name__ == '__main__':
    unittest.main()