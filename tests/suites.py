# Importamos el módulo unittest para trabajar con pruebas unitarias.
import unittest 

# Importamos la clase de pruebas BankAccountTests, que contiene las pruebas para la clase BankAccount.
from tests.test_bank_account import BankAccountTests

def bank_account_suite():
    """
    Esta función crea una suite de pruebas personalizada.
    Una suite es un contenedor que permite ejecutar múltiples pruebas de forma organizada.
    En este caso, estamos añadiendo pruebas específicas de la clase BankAccountTests.
    
    La función addTest permite especificar qué pruebas incluir en la suite.
    """
    # Creamos una instancia de TestSuite, que nos permitirá agregar las pruebas seleccionadas.
    suite = unittest.TestSuite()
    
    # Añadimos las pruebas específicas de la clase BankAccountTests.
    # Aquí estamos añadiendo las pruebas test_deposit y test_withdraw.
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    
    # Retornamos la suite con las pruebas añadidas.
    return suite

# Esta parte se ejecuta cuando se corre este archivo directamente.
# Aquí es donde se ejecutan las pruebas de la suite que hemos creado.
if __name__ == "__main__":
    """
    El runner es el componente que ejecuta las pruebas y muestra los resultados.
    En este caso, estamos utilizando el TextTestRunner que imprime los resultados de las pruebas en la consola.
    """
    runner = unittest.TextTestRunner()  # Creamos un objeto runner para ejecutar las pruebas.
    
    # Ejecutamos la suite de pruebas que hemos creado previamente.
    runner.run(bank_account_suite())  # Ejecutamos las pruebas en la suite.