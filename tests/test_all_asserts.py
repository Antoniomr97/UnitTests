import unittest

SERVER = "server_b"
# Importante que herede de TestCase de unittest para que con esta llamada python -m unittest discover -v -s tests se ejecuten los test (-v es opcional para mas información)
class AllAssertsTests(unittest.TestCase):

    def test_assert(self):

        self.assertEqual(10,10)
        self.assertEqual("Hola","Hola")

    def test_assert_true_or_false(self):

        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):

        # Comprobar si se lanzó un error
        with self.assertRaises(ValueError):
            int("No soy un número")

    def test_assert_in(self):

        # Valida si está en la lista el valor marcado
        self.assertIn(10, [2, 4, 5, 10])

        # Valida si el valor no está en la lista
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):

        user = {
            "first_name": "Antonio",
             "last_name": "Martínez"
             }
        
        # Comprueba que el usuario que devuelve es el que nosotros queremos
        self.assertDictEqual(
            {"first_name": "Antonio",
             "last_name": "Martínez"},
             user
        )

        # Comprueba que los dos sets de datos sean iguales
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
            )
    
    # Con unittest.skip no se realizará la prueba y devolverá el mensaje configurado, lo que puede ser util en ambientes de desarrollo
    @unittest.skip("En progreso, será habilitada proximamente")
    def test_skip(self):
        self.assertEqual("hola","adios")

    # Con unittest.skip no se realizará la prueba si la condicion se cumple
    @unittest.skipIf(SERVER == "server_b", "No se ha realizado esta prueba porque no estamos en el servidor correcto")
    def test_skip_if(self):
        self.assertEqual(100,100)

    # Con unittest.expectedFailure podemos controlar cuando esperamos que ocurra un error
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)
