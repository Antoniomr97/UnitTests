import unittest
from src.calculator import sum, subtract, multiplication, division  # Importa las funciones de la calculadora

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        """
        Prueba que la suma de dos números sea correcta.
        En este caso, se suma 2 y 3, y se espera que el resultado sea 5.
        """
        result = sum(2, 3)
        self.assertEqual(result, 5, "La suma no es correcta")

    def test_subtract(self):
        """
        Prueba que la resta de dos números sea correcta.
        En este caso, se resta 5 a 10, y se espera que el resultado sea 5.
        """
        result = subtract(10, 5)
        self.assertEqual(result, 5, "La resta no es correcta")

    def test_multiplication(self):
        """
        Prueba que la multiplicación de dos números sea correcta.
        En este caso, se multiplica 5 por 5, y se espera que el resultado sea 25.
        """
        result = multiplication(5, 5)
        self.assertEqual(result, 25, "La multiplicación no es correcta")
    
    def test_division(self):
        """
        Prueba que la división de dos números sea correcta.
        En este caso, se divide 25 entre 5, y se espera que el resultado sea 5.
        """
        result = division(25, 5)
        expected = 5
        self.assertEqual(result, expected, "La división no es correcta")

    def test_division_by_zero(self):
        """
        Prueba que la división entre cero lance un error adecuado.
        Se espera que se lance un ValueError cuando se intente dividir entre 0.
        """
        with self.assertRaises(ValueError, msg="Se esperaba un error al dividir entre cero"):
            division(10, 0)