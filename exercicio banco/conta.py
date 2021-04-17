from cliente import cliente
class conta:
    def __init__(self, saldo, limite, cliente):
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente
    def Sacar (self, sacar):
        if sacar > self.saldo + self.limite:
            print ('saldo insufuciente para saque, consulte seu saldo')
        else:
            self.saldo -= sacar
    def Depositar (self, depositar):
        self.saldo += depositar