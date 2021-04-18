'''
exercicio em que fiz um breve programa para contagem e organização em lista dos convidados de uma festa, nele trabalhei com estrutura de loop, listas e o acrescimo 
e remocao de elementos da lista durante a execucao do programa.
'''
lista_convidados = ['lista de convidados:']
# estrutura em loop para adicionar numero de convidados indeterminado, onde para encerrar o loop basta que o usuario digite "n"
for nome in lista_convidados:
    if nome == 'n':
        break
    lista_convidados.append(input('qual o nome do convidado? (se os convidados acabaram digite "n") '))
# remoção de "n" da lista ja que nao se trata de um convidado
lista_convidados.remove('n')
# exibe numero total de convidados com len -1 já que "lista de convidados:" n é um convidado
print ('total de convidados: \n', len (lista_convidados)-1)
# uso da estruturas em loop para exibir os nomes de convidados em lista
for nome in lista_convidados:
    print (nome)
