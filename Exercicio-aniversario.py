for nome in lista_convidados:
    if nome == 'n':
        break
    lista_convidados.append(input('qual o nome do convidado? (se os convidados acabaram digite "n") '))
lista_convidados.remove('n')
print ('total de convidados:','\n', len (lista_convidados)-1)
for nome in lista_convidados:
    print (nome)
