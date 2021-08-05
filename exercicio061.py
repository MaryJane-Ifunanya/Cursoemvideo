print('''\033[32mRefaça o DESAFIO 051, lendo o primeirotermo e a razão de 
uma PA, mostrando os 10 primeiros termos da programação usando a
estrutura while.\033[m''')
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro valor:'))
razao = int(input('Razão da PA:'))
termo = primeiro
c = 1
while c <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    c += 1
print('\033[34mFIM\033[m')
