print('''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão''')

print('='*40)
print('{:^40}'.format('\033[31m10 TERMOS DE UMA PA\033[m'))
print('='*40)
termo = int(input('Primeiro termo:'))
r = int(input('Razão:'))
decimo = termo + (10 - 1) * r
for c in range(termo, decimo + r, r):
    print('{}'.format(c), end=' →')
print('\033[33mACABOU\033[m')

