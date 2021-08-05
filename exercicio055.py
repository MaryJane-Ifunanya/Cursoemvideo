print('''Faça um programa que leia o peso de cinco pessoas.
No final , mostre qual foi o maior e o menor peso lidos.''')

maior = 0
menor = 0
for num in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:'.format(num)))
    if num == 1:
       maior = peso
       menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de \033[34m{:.1f}KG\033[m'.format(maior))
print('O menor peso lido foi de \033[34m{:.1f}KG\033[m'.format(menor))
