print('''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo''')
cont = 0
num = int(input('Digite um numero:'))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vazes'.format(num, cont))
if cont == 2:
    print('E por isso ele é \033[35mPRIMO!\033[m')
else:
    print('E por isso ele não é \033[35mPRIMO!\033[m')

