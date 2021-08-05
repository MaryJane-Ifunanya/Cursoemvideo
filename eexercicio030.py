print('''Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR OU IMPAR.''')
número = int(input('Me diga um número:'))
resultado = número % 2#na matematica, o resto da divisao de qualquer num par por 2 é 0 e por qualquer num impar é igual a 1.
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))