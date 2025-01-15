# Excepción personalizada para manejar intentos de retiro fuera del horario permitido.
class WithdrawalTimeRestrictionError(Exception):
    """
    Excepción que se lanza cuando un intento de retiro se realiza fuera del horario permitido
    (8 AM - 5 PM).
    """
    pass