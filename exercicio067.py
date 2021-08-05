print('''\033[34mFaça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.\033[m''')

while True:
    n = int(input('Quer ver a tabuade de que valor?'))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n*c:2}')
    print('-' * 30)
print('\033[33mPROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!\033[m')

