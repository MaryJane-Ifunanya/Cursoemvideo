print('''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Qantas letras tem o primeiro nome.''')

nome = str(input('Digite o seu nome:')).strip()
print('Analisando o seu nome...')
print('seu nome maiúscula é {}'.format(nome.upper()))
print('Seu nome minúscula é {}'.format(nome.lower()))
print('Seu primeiro tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
