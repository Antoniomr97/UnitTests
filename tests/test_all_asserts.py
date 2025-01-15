# Importamos unittest, que es el módulo estándar de Python para realizar pruebas unitarias.
import unittest

# Definimos una constante para simular el nombre de un servidor (esto es solo un ejemplo para tests condicionales).
SERVER = "server_b"

# Es importante que nuestra clase herede de unittest.TestCase para que funcione correctamente con el marco de pruebas.
# Al heredar de TestCase, podemos aprovechar los métodos de aserción proporcionados por unittest.
class AllAssertsTests(unittest.TestCase):

    def test_assert(self):
        """
        Este método verifica que dos valores sean iguales usando assertEqual.
        Verifica que 10 sea igual a 10 y que el string "Hola" sea igual a "Hola".
        """
        self.assertEqual(10, 10)  # Verifica que 10 sea igual a 10
        self.assertEqual("Hola", "Hola")  # Verifica que el string "Hola" sea igual a "Hola"

    def test_assert_true_or_false(self):
        """
        Este método verifica si los valores dados son verdaderos o falsos usando assertTrue y assertFalse.
        """
        self.assertTrue(True)  # Verifica que la expresión sea verdadera
        self.assertFalse(False)  # Verifica que la expresión sea falsa

    def test_assert_raises(self):
        """
        Verifica si se lanza una excepción. En este caso, espera que se lance un ValueError
        cuando intentamos convertir un string no numérico en entero.
        """
        with self.assertRaises(ValueError):  # Verifica que se lance un ValueError
            int("No soy un número")

    def test_assert_in(self):
        """
        Verifica si un valor está o no dentro de una colección (lista en este caso) utilizando assertIn y assertNotIn.
        """
        self.assertIn(10, [2, 4, 5, 10])  # Verifica que 10 esté en la lista [2, 4, 5, 10]
        self.assertNotIn(5, [2, 4, 10])  # Verifica que 5 no esté en la lista [2, 4, 10]

    def test_assert_dicts(self):
        """
        Compara diccionarios usando assertDictEqual y sets usando assertSetEqual.
        Verifica si dos diccionarios o sets son iguales.
        """
        user = {  # Definimos un diccionario con datos de usuario
            "first_name": "Antonio",
            "last_name": "Martínez"
        }
        
        # Verifica que el diccionario esperado sea igual al diccionario obtenido
        self.assertDictEqual(
            {"first_name": "Antonio", "last_name": "Martínez"},
            user
        )

        # Verifica que los dos sets sean iguales
        self.assertSetEqual({1, 2, 3}, {1, 2, 3})  # Verifica que los sets sean iguales

    # Uso del decorador unittest.skip para saltar una prueba, útil cuando no se puede realizar aún.
    @unittest.skip("En progreso, será habilitada proximamente")
    def test_skip(self):
        """
        Esta prueba es saltada debido al decorador @unittest.skip, y muestra el mensaje especificado.
        """
        self.assertEqual("hola", "adios")  # Esta línea nunca se ejecutará debido al decorador

    # Uso del decorador unittest.skipIf para saltar la prueba si se cumple la condición especificada.
    @unittest.skipIf(SERVER == "server_b", "No se ha realizado esta prueba porque no estamos en el servidor correcto")
    def test_skip_if(self):
        """
        Esta prueba se saltará si la variable SERVER es igual a 'server_b', y se mostrará el mensaje dado.
        """
        self.assertEqual(100, 100)  # Esta prueba no se ejecutará si SERVER == "server_b"

    # Uso del decorador unittest.expectedFailure para marcar una prueba que esperamos que falle.
    @unittest.expectedFailure
    def test_expected_failure(self):
        """
        Esta prueba está marcada como una falla esperada. El marco de pruebas la marcará como fallida sin considerarla un error.
        """
        self.assertEqual(100, 150)  # Esperamos que esta comparación falle, por lo que la marcamos como una falla esperada