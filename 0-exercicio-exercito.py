'''
neste exercicio, simulei um programa para avaliar a apitidao de possiveis candidatos a entrar no exercito, porém sem o uso dos criterios reais, nele pude trabalhar
com operações logicas, comparações, bem como diferentes tipos de tipos de dados.
'''
#primeiro solicito ao usuario os valores das variaveis utilizadas com o imput, e as converto de string para boolean, float e integer
idade = int (input ('qual sua idade? '))
peso = float (input ('qual o seu peso? '))
altura = float (input ('qual sua altura? '))
homem = bool (input ('voce é homem? '))
#então retorno para o usuario com print a resposta adeguada segundo os dados fornecidos e o uso do if else e and para a comparacao
if idade > 18 and idade < 30 and peso >= 60 and peso < 80 and altura >= 1.70 and homem == True:
    print ('voce esta apto a entrar no exercito')
else:
    print ('voce não esta apto a entrar no exercito')
