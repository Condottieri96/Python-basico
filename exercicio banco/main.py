'''
exercicio para gerenciar dados de clientes em um banco, exercicio para introducao a orientacao a objeto
'''
# importando objeto das bibliotecas criadas "cliente" e "conta"
from conta import conta
from cliente import cliente
# criando conta e cliente para o exercicio
cliente1 = cliente ('joao', 42, 2045)
conta1 = conta (40, 50, cliente1)
#testes para ver se os objetos e funcoes estao funcionando como previsto
print (conta1.saldo)
conta1.Depositar (50)
print (conta1.saldo)
conta1.Sacar (140)
print (conta1.saldo)
conta1.Sacar (1)
