'''
funções para determinar o maior e o menor numero de uma colecao, neste exercicio pude praticar a criacao de novas funcoes que nao estao originalmente presentes no
python, 
'''
#funcao para encontrar o maior numero em uma colecao
def maior_numero (x):
    numero_anterior = x[0]
    for numero in x:
        if numero > numero_anterior:
            numero_anterior = numero
    return numero_anterior
#funcao para encontrar o menor numero em uma colecao
def menor_numero (x):
    numero_anterior = x[0]
    for numero in x:
        if numero < numero_anterior:
            numero_anterior = numero
    return numero_anterior
#lista inicial onde o usuario colocara os numeros, o elemento "a" presente esta ai apenas para dar inicio a primenira estrutura de loop
lista = ['a']
for numero in lista:
    if numero == 'n':
        break
    lista.append(input('adicione um numero: (se os numeros acabaram digite "n") '))
#remocao de "n" e "a" pois não são numeros reais e nao podem ser convertidos para integer
lista.remove ('n')
lista.remove ('a')
#criação da lista que sera usada ao final e converção das strings para integer
listaFinal = []
for numero in lista:
    listaFinal.append(int(numero))
# devolucao para o usuario do maior e menor numero da colecao
print ('o maior numero da lista é: ', maior_numero(listaFinal))
print ('o menor numero da lista é: ', menor_numero(listaFinal))
