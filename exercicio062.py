print('''Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.''')
print('Gerador de PA')
print('-='* 10)
first = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = first
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))