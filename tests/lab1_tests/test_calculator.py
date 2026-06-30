import unittest
from src.lab1.calculator import calculate

class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_sub(self):
        self.assertEqual(calculate(10, 4, "-"), 6)

    def test_mul(self):
        self.assertEqual(calculate(3, 4, "*"), 12)

    def test_div(self):
        self.assertEqual(calculate(10, 2, "/"), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, "/")

    def test_pow(self):
        self.assertEqual(calculate(2, 3, "**"), 8)

    def test_unknown_op(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "%")