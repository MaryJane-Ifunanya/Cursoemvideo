print('''Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.''')

'''dias = int(input('Quantos dias alugados?'))
km= float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O preço a pagar é de R$\033[31m{:.2f}\033[m'.format(pago))'''#ou

dias = int(input('Quantos dias?'))
km = float(input('Quantos km rodados?'))
c = 60
k = 0.15
print('O total a pagar é de R${:.2f}!'.format((dias*c) + (km*k)))
