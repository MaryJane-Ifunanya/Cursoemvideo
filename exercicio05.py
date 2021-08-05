print('''Faça um programa que leia um número inteiro e mostre na 
tela o seu sucessor e seu antecessor.''')

n = int(input('Digite um número:'))

print('Analisando o  valor \033[35m{}\033[m, seu antecessor é \033[32m{}\033[m e o sucessor é \033[34m{}\033[m'.format(n, (n-1),(n+1)))
