print('''Faça um programa que leia o preço de um produto e 
mostre seu novo preço com 5% de desconto.''')

preco = float(input('Qual é o preço do produto?'))
novo = preco - (preco * 5/100)
print('O produto que custava {:.2f} na promoção com disconto de 5% vai custar \033[34mR${:.2f}\033[m'.format(preco, novo))
