print('''Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ele pode comprar.''')

dinheiro = float(input('Quanto você tem na carteira? R$'))
real = dinheiro / 5.48
print('Com \033[32m{:.2f}\033[m você pode comprar US$\033[36m{:.3f}\033[m'.format(dinheiro, real))
