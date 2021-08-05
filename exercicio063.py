print('''\033[32mEscreva um programa que leia um número inteiro qualquer e 
mostre na tela os primeiros elementos de uma Sequência de Fibonacci.\033[m''')
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar?'))
print('~' * 30)
p1 = 0
p2 = 1
print('{} → {}'.format(p1, p2), end='')
cont = 3
while cont <= termos:
    p3 = p1 + p2
    print('→ {}'.format(p3),end='')
    p1 = p2
    p2 = p3
    cont += 1
print('→ FIM')
print('~' * 30)