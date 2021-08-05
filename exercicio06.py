print('Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

n = int(input('Digite um numero:'))
print('O dobro de {} é \033[34m{}\033[m'.format(n,(n*2)))
print('O tripulo de {} é \033[34m{}\033[m'.format(n,(n*3)))
print('A raiz quadrada de {} é \033[34m{:.2f}\033[m'.format(n,(n**(1/2))))