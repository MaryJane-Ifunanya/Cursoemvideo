print('''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele \033[32mainda vai se alistar\033[m ao serviço militar,
se é a \033[32mhora de se alistar\033[m ou seja já \033[32mpassou o tempo do alistamento\033[m.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.''')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem \033[36m{}\033[m anos em \033[34m{}\033[m.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:#ou else
    saldo =idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
