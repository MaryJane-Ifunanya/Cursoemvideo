print('''Crie um programa que leia uma frase qualquer e diga se ela é um palindroma,
desconsiderando os espaços''')

frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso = junto[::-1]     #ou utilizamos o "FOR"
'''for letra in range(len(junto) - 1, -1, -1):
    inverso+= junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[34mTemos um palíndromo!\033[m')
else:
    print('A frase digitada \033[31mnão é um palíndromo!\033[m')

