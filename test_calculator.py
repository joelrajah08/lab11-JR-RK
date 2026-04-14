import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(2, 7), -5)
        self.assertEqual(sub(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 25), 5)
        self.assertRaises(ZeroDivisionError, divide, 0, 5)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(3, 9), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm, -1, 10)
        self.assertRaises(ValueError, logarithm, 2, -5)
        self.assertRaises(ValueError, logarithm, 0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 5), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertRaises(ValueError, square_root, -1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()