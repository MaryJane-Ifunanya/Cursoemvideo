print('''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se eles podem ou não formar um triângulo.''')

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeiro segmento:'))
n2 = float(input('Segundo segmento:'))
n3 = float(input('Terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2: #o terceiro valor tem que ser menor que os 2 anteriores
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triângulo!')

