print('''\033[34mCrie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário quer continuar. No final, mostre:
[ A ] Qual foi o total gasto na compra.
[ B ] Quantos produtos custam mais de R$1000.
[ C ] Qual é o nome do produto mais barato.\033[m''')

custoMaior = menor = cont = total = 0
nomedoP = ''
while True:
    print('-' * 30)
    print('{:^30}'.format('\033[32mLOJA SUPER BARATÃO\033[m'))
    print('-' * 30)
    produto = str(input('Nome do Produto:'))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if preco > 1000:
        custoMaior += 1
    if cont == 1: #ou podemos usar assim "if cont == 1 or preco < menor:" e tirar o else.
        menor = preco
        nomedoP = produto
    else:
        if preco < menor:
            menor = preco
            nomedoP = produto
    if resp == 'N':
        break
print(f'O total da compra foi de R$\033[32m{total:.2f}\033[m')
print(f'Temos \033[32m{custoMaior}\033[m produto custando mais de R$1000.00')
print(f'O produto mais barato foi \033[32m{nomedoP}\033[m que custa \033[32m{menor:.2f}\033[m')