print('''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.''')

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
  print('MULTADO! você excedeu o limite permitido que é de 80Km/h')
  multa = (velocidade -80) * 7#cada km é R$7, entao a velocidade menus o 80 ai reslt*7
  print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')