def maior_numero (x):
    numero_anterior = x[0]
    for numero in x:
        if numero > numero_anterior:
            numero_anterior = numero
    return numero_anterior
def menor_numero (x):
    numero_anterior = x[0]
    for numero in x:
        if numero < numero_anterior:
            numero_anterior = numero
    return numero_anterior
lista = [0, 2, 3, -1]
print ('o maior numero da lista é: ', maior_numero(lista))
print ('o menor numero da lista é: ', menor_numero(lista))
