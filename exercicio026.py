print('''Faça um programa que leia uma frase pelo teclado e mostra:
-Quantas vezes apareceu a letra "A".
-Em que posição ela aparece a primeira vez.
-Em que posição ela aparece a último vez.''')

frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('A primeira A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))