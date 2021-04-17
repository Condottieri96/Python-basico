idade = float (input ('qual sua idade? '))
peso = float (input ('qual o seu peso? '))
altura = float (input ('qual sua altura? '))
homem = bool (input ('voce é homem? '))
if idade > 18 and idade < 30 and peso >= 60 and peso < 80 and altura >= 1.70 and homem == True:
    print ('voce esta apto a entrar no exercito')
else:
    print ('voce não esta apto a entrar no exercito')
