print('''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.''')
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for ano in range(1, 8):
    num = int(input('Em que ano a {}ª pessoa nasceu?'.format(ano)))
    idade = atual - num
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

