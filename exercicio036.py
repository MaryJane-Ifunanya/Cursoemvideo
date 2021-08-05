print('''Ecsreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. Pergunte o \033[33mvalor da casa\033[m, o \033[33msalário\033[m
do comprador e em \033[33mquantos anos\033[m ele vai pagar.
A prestação mensal, não pode exceder \033[33m30%\033[m do salário ou então
o empréstimo será negado.''')

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar?'))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$\033[32m{:.2f}\033[m'.format(prestacao))
if prestacao <= minimo:
    print('\033[34mEMPRÉSTIMO pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[m')