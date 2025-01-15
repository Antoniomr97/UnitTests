import unittest
import os
from unittest.mock import patch
from src.exceptions import WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    # setUp se ejecuta antes de cada prueba, inicializando el objeto BankAccount
    def setUp(self) -> None:
        """
        Configura el entorno para cada prueba, creando una instancia de BankAccount 
        con un saldo inicial de 1000 y un archivo de registro de transacciones.
        """
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    # tearDown se ejecuta después de cada prueba, eliminando el archivo de registro si existe
    def tearDown(self):
        """
        Limpia el entorno después de cada prueba, eliminando el archivo de registro
        de transacciones si fue creado durante la prueba.
        """
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    # Función auxiliar para contar las líneas en un archivo, útil para verificar el número de transacciones
    def _count_lines(self, filename):
        """
        Cuenta el número de líneas en un archivo de texto. Se utiliza para verificar
        el número de transacciones registradas.
        """
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        """
        Prueba que el método 'deposit' actualice correctamente el saldo de la cuenta.
        En este caso, se deposita 500 y se espera que el saldo total sea 1500.
        """
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        """
        Prueba que el método 'withdraw' actualice correctamente el saldo después de un retiro.
        En este caso, se retiran 200 y se espera que el saldo total sea 800.
        """
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):
        """
        Prueba que el método 'get_balance' devuelva el saldo correcto de la cuenta.
        Se espera que el saldo inicial sea 1000.
        """
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transaction_log(self):
        """
        Prueba que el archivo de registro de transacciones se cree cuando se realiza un depósito.
        Se espera que el archivo 'transaction_log.txt' exista después de realizar un depósito.
        """
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        """
        Prueba que el número de transacciones registradas en el archivo de log sea correcto.
        Se verifica que después de un depósito, el archivo tenga exactamente 2 líneas.
        """
        assert self._count_lines(self.account.log_file) == 1  # Verifica una transacción inicial
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2  # Verifica que la transacción se haya registrado

    @patch("src.bank_account.datetime")
    def test_withdraw_during_business_hours(self, mock_datetime):
        """
        Prueba que el retiro sea permitido durante las horas laborales (por ejemplo, de 9:00 a 18:00).
        Se simula la hora como las 10:00 AM y se espera que el retiro se complete correctamente.
        """
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_business_hours(self, mock_datetime):
        """
        Prueba que el retiro sea bloqueado antes de las horas laborales (por ejemplo, antes de las 9:00).
        Se simula la hora como las 7:00 AM y se espera que se lance una excepción.
        """
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        """
        Prueba que el retiro sea bloqueado después de las horas laborales (por ejemplo, después de las 18:00).
        Se simula la hora como las 20:00 (8:00 PM) y se espera que se lance una excepción.
        """
        mock_datetime.now.return_value.hour = 20
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    def test_deposit_multiple_amounts(self):
        """
        Prueba el método 'deposit' con múltiples cantidades de depósito.
        Se verifica que el saldo se actualice correctamente después de cada depósito.
        """
        test_cases = [
            {"ammount": 100, "expected": 1100},  # Primer caso, saldo esperado: 1100
            {"ammount": 3000, "expected": 4000},  # Segundo caso, saldo esperado: 4000
            {"ammount": 4500, "expected": 5500},  # Tercer caso, saldo esperado: 5500
        ]
        
        # Itera sobre los diferentes casos de prueba usando subTest para cada cantidad
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])