print('''\033[34mCrie um programa que leia a idade e o sexo de
várias pessoas. A cadapessoa cadastrada, o programa deverá perguntar
se o usuario quer continuar. No final, mostre:
[ 1 ] Quantas pessoas tem mais de 18 anos.
[ 2 ] Quantos homens foram cadastrados.
[ 3 ] Quantas mulheres tem menos de 20 anos.\033[m''')

maior = tothomem = totMmenor =  0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        print('-' * 20)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totMmenor += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {tothomem} homens cadastrados.')
print(f'E temos {totMmenor} mulheres com menos de 20 anos.')


