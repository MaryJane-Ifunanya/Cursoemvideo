print('''\033[32mCrie um programa que leia dois valores e mostre um menu
como o abixo :
seu programa deverá realizar a operação solicitada em cadacaso.
[ 1 ]somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos números
[ 5 ]sair do programa\033[m
----------------------------------------''')
from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
menu = 0
while menu != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    menu = int(input('>>>>> Qual é a sua opção?'))
    if menu == 1:
        print('A soma entre {} e {} é \033[34m{}\033[m'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('O resultado de {} e {} é \033[34m{}\033[m'.format(n1, n2, n1*n2))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é \033[34m{}\033[m'.format(n1, n2, maior))
    elif menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif menu == 5:
        print('\033[33mFinalizando...\033[m')
    else:
        print('\033[31mOpção inválida. Tente novamente!\033[m')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')