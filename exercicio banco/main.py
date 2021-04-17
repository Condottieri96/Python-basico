from conta import conta
from cliente import cliente
cliente1 = cliente ('joao', 42, 2045)
conta1 = conta (40, 50, cliente1)

print (conta1.saldo)
conta1.Depositar (50)
print (conta1.saldo)
conta1.Sacar (140)
print (conta1.saldo)
conta1.Sacar (1)