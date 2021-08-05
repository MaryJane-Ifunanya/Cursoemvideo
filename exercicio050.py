print('''Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que foram pares. Se o valor
digitado for impar, desconsidere-o.''')
soma = 0
cont = 0
for n in range(1, 7):
    numero = int(input('Digite o {} valor:'.format(n)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('VOCÊ INFORMOU {} numeros \033[31mPARES\033[m e a soma for \033[34m{}\033[m'.format(cont, soma))
