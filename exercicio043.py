print('''Desenvolva uma lógica que leia o peso de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
[ 1 ] Abaixo de 18.5: Abaixo de peso
[ 2 ] Entre 18.5 e 25: Peso ideal
[ 3 ] 25 até 30: Sobrepeso
[ 4 ] 30 até 40: Obesidade
[ 5 ] Acima de 40: Obesiade mórbida''')

peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está \033[34mABIXO\033[m DO PESO normal')
elif 18.5 <= imc < 25: #imc >= 18.5 and imc < 25:
    print('\033[34mPARABÉNS, Você está na faixa de PESO NORMAL\033[m')
elif 25 <= imc < 30:
    print('Você está em \033[36mSOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('Você está em \033[35mOBESIDADE!\033[m')
elif imc >= 40:
    print('Você está em \033[31mOBESIDADE MôRBIDA, cuidado!\033[m')

