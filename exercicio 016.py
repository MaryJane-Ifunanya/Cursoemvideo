print('''Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
EX: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.''')

'''from math import trunc
num = float(input('Digite um numero:'))
print('O numero:{} tem a parte inteira {}'. format(num,trunc(num)))'''

nim = float(input('Digite um numero:'))
print('O valor digitado foi {} e a sua porcao inteira foi \033[34m{}\033[m'.format(nim, int(nim)))

