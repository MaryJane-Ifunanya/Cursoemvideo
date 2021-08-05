print('''Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possiveis sobre ele.''')

a = input('Digite algo:')
print('O tipo primitivo desse valor é','\033[34m', type(a),'\033[m')
print('Só tem espaços?','\033[31m',a.isspace(),'\033[m')
print('É um numero?', '\033[33m',a.isnumeric(),'\033[m')
print('É alfabético?','\033[32m',a.isalpha(),'\033[m')
print('É alfanumérico?','\033[35m',a.isalnum(),'\033[m')
print('Está em maiúscuças?','\033[36m', a.isupper(),'\033[m')
print('Está em minúsculas?','\033[30m',a.islower(),'\033[m')
print('Está em capitalizada?','\033[35m', a.capitalize(),'\033[m')

