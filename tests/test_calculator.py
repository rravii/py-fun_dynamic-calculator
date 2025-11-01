import unittest
from src.calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_numbers(self):
        print("Running test_add_numbers")
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add("1", "2"), 3)
        self.assertEqual(self.calc.add("three", "four"), 7)

    def test_sub_numbers(self):
        print("Running test_sub_numbers")
        self.assertEqual(self.calc.sub(5, 3), 2)

    def test_mul_numbers(self):
        print("Running test_mul_numbers")   
        self.assertEqual(self.calc.mul(3, 4), 12)

    def test_div_numbers(self):
        print("Running test_div_numbers")
        self.assertEqual(self.calc.div(8, 2), 4)

if __name__ == "__main__":
    unittest.main()
