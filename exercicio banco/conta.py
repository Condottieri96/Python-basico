#criacao do objeto conta, para isso se importa os a funcao cliente do arquivo cliente
from cliente import cliente
#criaçao do objeto conta e delimitacao dos seus atributos
class conta:
    def __init__(self, saldo, limite, cliente):
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente
    #definicao do funcao sacar dentro do objeto conta
    def Sacar (self, sacar):
        if sacar > self.saldo + self.limite:
            print ('saldo insufuciente para saque, consulte seu saldo')
        else:
            self.saldo -= sacar
    #definicao da funcao depositar dentro do objeto conta
    def Depositar (self, depositar):
        self.saldo += depositar
