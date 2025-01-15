import unittest 
from tests.test_bank_account import BankAccountTests

def bank_account_suite():
    # Creamos una suite para añadirle pruebas determinadas
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite

# Para poner en funcionamiento los tests seleccionados
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())