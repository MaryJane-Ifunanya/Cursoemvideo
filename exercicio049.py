print('''Refaça o DESAFIO009, mostrando a tabuada de um número que o usuário escolher,
sé que agora utilizando um laço FOR''')

numero = int(input('Digite um numero para ver sua tabuada:'))
for n in range(1, 11):
    print('{} x {:2} = \033[34m{}\033[m'.format(numero, n, numero*n))
