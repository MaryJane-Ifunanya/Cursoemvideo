print('''Crie um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.''')
from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
vitoria = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 10)
    soma = computador + jogador
    play = ' '
    while play not in 'PI':
        play = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('-' * 40)
    print(f'Você jogou \033[32m{jogador}\033[m e o computador \033[32m{computador}\033[m. Total de {soma} ', end='')
    print('\033[34m DEU PAR\033[m' if soma % 2 == 0 else '\033[34mDEU IMPAR\033[m')
    print('-' * 40)
    if play == 'P':
        if soma % 2 == 0:
            print('\033[1;34mVOCÊ VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    elif play == 'I':
        if soma % 2 == 1:
            print('\033[1;34mVOCÊ VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
        print('=-' * 20)
    print('Vamos jogar novamente...')
print('=-' * 20)
print(f'GAME OVER! Você venceu \033[32m{vitoria}\033[m vezes.')

