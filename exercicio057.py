print('''Faça um programa que leia o \033[32msexo\033[m de uma pessoa,
mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação
novamente até ter um valor correto.''')

n = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while n not in 'MmFf':
    n = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrada com sucesso'.format(n))
