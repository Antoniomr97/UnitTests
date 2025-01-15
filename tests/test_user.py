import unittest, os
from faker import Faker
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):
    # Creamos una instancia de Faker
    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        # Creamos un usuario con nombre y correo falsos
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_creation(self):
        # Generamos un nombre y correo falso
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        
        # Verificamos que el usuario haya sido creado con los datos correctos
        self.assertEqual(user.name, name_generated, f"El nombre esperado era {name_generated}, pero se obtuvo {user.name}")
        self.assertEqual(user.email, email_generated, f"El correo esperado era {email_generated}, pero se obtuvo {user.email}")

    def test_user_with_multiple_account(self):
        # Añadimos varias cuentas al usuario
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_accounts(account=bank_account)

        # Verificamos que el saldo total del usuario sea igual a la suma de los saldos de las cuentas
        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value, f"El saldo total esperado es {expected_value}, pero se obtuvo {value}")

    def tearDown(self):
        # Eliminamos los archivos de log creados durante las pruebas
        for account in self.user.accounts:
            if os.path.exists(account.log_file):  # Comprobamos que el archivo existe antes de eliminarlo
                os.remove(account.log_file)