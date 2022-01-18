class accountbank:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    name = "Interbank"
    accounts = []
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        accountbank.accounts.append(self)
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def depósito(self, amount): 
        # tu código aquí
        self.balance += amount
        return self

    def retiro(self, amount):
        # tu código aquí
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        # tu código aquí
        print(f"Balance: {self.balance}")

    def generar_interés(self):
        # tu código aquí
        self.balance += self.balance * self.tasa_interés
        return self

    @classmethod
    def mostrar_informacion_banco(cls):
        for account in cls.accounts:
            account.mostrar_info_cuenta()
        

