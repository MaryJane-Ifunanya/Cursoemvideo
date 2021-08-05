print('''Escreva um programa que converte uma temperatura digitado em ºC 
e converta para ºF.''')

c = float(input('Informe a temperatura em °C:'))
f = ((9*c)/5)+32
print('A temperatura de {}°C correspnde a \033[31m{}\033[m°F!'.format(c, f))
