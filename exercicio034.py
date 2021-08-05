print('''Escreva um programa que pergunte o salário de um funcionario e
 calcule o valor do seu aumento.
 Para salário superiores a \033[37mR$250.00\033[m, calcule um aumento de
 \033[37m10%\033[m. Para os inferiores ou iguais, o aumento é de \033[37m15%\033[m.''')

salario = float(input('Qual é o salário do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${} passa a ganhar R${} agora.'.format(salario, novo))

