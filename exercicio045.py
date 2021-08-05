print('''Crie um programa que faça o computador jogar jokenpô com você.''')
from random import randint
from time import sleep
itens = ['Pedra','Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('\033[36mJO\033[m')
sleep(1)
print('\033[36mKEN\033[m')
sleep(1)
print('\033[36mPO!!!\033[m')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('\033[32mEMPATE\033[m')
    elif jogador == 1:
        print('\033[34mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[34mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('\033[34mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[32mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[34mJOGADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\03[m')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('\033[34mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[34mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[32mEMPATE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
