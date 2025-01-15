import unittest
from src.calculator import *

class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        assert sum( 2 , 3) == 5

    def test_subtract(self):
        assert subtract( 10 , 5) == 5

    def test_multiplication(self):
        assert multiplication(5 , 5) == 25
    
    def test_division(self):
        result = division(25,5)
        expected = 5
        assert result == expected

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(10,0)