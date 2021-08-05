print('''Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento. ''')

salario = float(input('Qual é o seu salario? R$'))
novo = salario + (salario * 15/100)
print('Um funcionario que ganhava R${}, com aumento de 15%, passa a ganhar \033[32mR${}\033[m'.format(salario, novo))
