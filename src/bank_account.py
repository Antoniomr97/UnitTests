from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError

# Clase que representa una cuenta bancaria con funcionalidades de depósito, retiro y consulta de saldo
class BankAccount:
    def __init__(self, balance=0, log_file=None):
        """
        Inicializa la cuenta bancaria con un saldo inicial y un archivo de registro opcional.

        Parámetros:
        - balance: El saldo inicial de la cuenta (por defecto es 0).
        - log_file: La ubicación del archivo de registro donde se guardarán las transacciones (opcional).
        """
        self.balance = balance
        self.log_file = log_file
        
        # Registra la creación de la cuenta en el archivo de log si está habilitado
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        """
        Método privado para registrar las transacciones en el archivo de log.

        Parámetros:
        - message: El mensaje de la transacción que se va a registrar.
        """
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        """
        Realiza un depósito en la cuenta si el monto es positivo.

        Parámetros:
        - amount: El monto a depositar en la cuenta (debe ser mayor que 0).

        Retorna:
        - El nuevo saldo después de realizar el depósito.

        Si el monto es negativo o cero, no realiza el depósito.
        """
        if amount > 0:
            self.balance += amount
            # Registra la transacción de depósito
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        """
        Realiza un retiro de la cuenta, asegurándose de que sea dentro del horario permitido
        (de 8 AM a 5 PM). Si el retiro se realiza fuera de este horario, se lanza una excepción.

        Parámetros:
        - amount: El monto a retirar de la cuenta (debe ser mayor que 0).

        Retorna:
        - El nuevo saldo después de realizar el retiro.

        Lanza una excepción si el intento de retiro se realiza fuera del horario permitido.
        """
        # Comprobamos la hora actual para asegurarnos de que el retiro esté dentro del horario permitido
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")

        if amount > 0:
            self.balance -= amount
            # Registra la transacción de retiro
            self._log_transaction(f"Withdrew: {amount}. New balance {self.balance}")
        return self.balance

    def get_balance(self):
        """
        Obtiene el saldo actual de la cuenta y lo registra en el archivo de log si está habilitado.

        Retorna:
        - El saldo actual de la cuenta.
        """
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance