print('''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e 
R$0.45 para viagens mais longa.''')

distancia = float(input('Qual é a distancia da sua viagem?'))
print('Você está preste a começar uma viagem de {}Km.'.format(distancia))
#if distancia <=200:
    #preço = distancia * 0.50
#else:
    #preço = distancia * 0.45''' #agente pode fazer esse mesmo exemplo simplificado
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('E o preço da sua viagem será de R${}'.format(preço))
