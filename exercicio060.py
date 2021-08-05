print('''\033[32mFaça um programa que leia um número qualquer e
 mostre o seu fatorial.\033[m
----------------------------------------------''')
n = int(input('Digite um número para calcular seu Fatorial:'))
f = 1
count = n
print('Calculando {}! = '.format(n), end='')
while count > 0:# ou podemos uzar a bibloteca math.
    print('{}'.format(count), end='')
    print(' X ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print('{}'.format(f), end='')

