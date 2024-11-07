import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertNotEqual(self.calc.add(1, 2), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertNotEqual(self.calc.subtract(8, 2), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertNotEqual(self.calc.multiply(1, 2), 1)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertNotEqual(self.calc.divide(4, 2), 3)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
        self.assertNotEqual(self.calc.modulo(4, 3), 3)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)