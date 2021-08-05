print('Crie um programa que leia dois números e mostre a soma entre eles.')

n1 = input('Digite um valor:')
n2 = input('Digite outro valor:')
soma = n1 + n2
print('A soma entre \033[31m{}\033[m e \033[34m{}\033[m é igual a \033[4;35m{}\033[m!'.format(n1, n2, soma))