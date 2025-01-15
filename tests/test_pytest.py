import pytest
from src.bank_account import BankAccount
import os

# Definimos los valores a probar usando parametrize
@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),  # 100 + 1000 = 1100
    (3000, 4000), # 3000 + 1000 = 4000
    (4500, 5500)  # 4500 + 1000 = 5500
])
def test_deposit_varios_ammounts(ammount, expected):
    """
    Prueba de depósito para diferentes montos.
    Este test verifica que al realizar un depósito en la cuenta,
    el saldo resultante sea el esperado.
    """
    # Creamos una nueva instancia de BankAccount con saldo inicial
    account = BankAccount(balance=1000, log_file="transactions.txt")
    
    # Realizamos el depósito
    new_balance = account.deposit(ammount)
    
    # Verificamos que el saldo nuevo sea igual al saldo esperado
    assert new_balance == expected, f"El saldo esperado era {expected}, pero se obtuvo {new_balance}"
    
    # Limpiamos el archivo de registro después de cada test para evitar que se acumule información
    if os.path.exists(account.log_file):
        os.remove(account.log_file)