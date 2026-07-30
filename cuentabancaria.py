class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):

        if cantidad > 0: self.__saldo += cantidad 
        
        else: 
            print("La cantidad a depositar debe ser positiva")


    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad 
            print(f"Su nuevo saldo es: {self.__saldo}")

        else:
            print("Fondos insuficientes")

    def ver_saldo(self):
        print(f"El saldo de {self.titular} es: {self.__saldo}")


Jose1 = CuentaBancaria("Laura", 100000)
Jose1.depositar(300000)
Jose1.ver_saldo()  # Debería mostrar 150000
Jose1.retirar(80000)
Jose1.ver_saldo()  # Debería mostrar 130000