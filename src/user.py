class User:
    # El constructor (__init__) se usa para inicializar un nuevo objeto de tipo User.
    def __init__(self, name, email):
        # Al crear un nuevo objeto User, se asignan el nombre y el correo electrónico proporcionados.
        self.name = name
        self.email = email
        # Inicializa una lista vacía de cuentas asociadas al usuario.
        self.accounts = []

    # Método para añadir una cuenta al usuario.
    def add_accounts(self, account):
        # Agrega una cuenta a la lista de cuentas del usuario.
        self.accounts.append(account)

    # Método para calcular el saldo total de todas las cuentas del usuario.
    def get_total_balance(self):
        # Suma el saldo de todas las cuentas asociadas al usuario y lo devuelve.
        # Para cada cuenta en self.accounts, se llama a get_balance() para obtener el saldo de cada cuenta.
        return sum(account.get_balance() for account in self.accounts)