print('''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
[ 1 ] Á vista dinheiro/cheque: 10% de desconto
[ 2 ] Á vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')

print('{:=^40}'.format(' LOJAS MARYJANE '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ]á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$\033[35m{:.2f}\033[m SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$\033[32m{:.2f}\033[m COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar R$\033[34m{:.2f}\033[m no final.'.format(preço, total))

