print('''Faça um programa que leia a soma entre todos os números impares,
que são múltiplos de três e que se encontram no intervalo de 1 até 500.''')
soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
       soma = soma + impar           #ou  += impar
       cont = cont + 1               #ou  += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

