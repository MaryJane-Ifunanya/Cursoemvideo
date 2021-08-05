print('''Escreva um programa que leia \033[34mdois números\033[m inteiros e compare-os,
mostrando na tela uma mensagem:
-O \033[33mprimeiro \033[m é \033[34mmaior\033[m
-O \033[33msegundo valor\033[m é \033[34mmaior\033[m
-\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m''')

n1 = int(input('Primeiro numero:'))
n2 = int(input('Segundo numero:'))
if n1 > n2:
    print('O \033[35mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[35mSEGUNDO\033[m valor é maior')
elif n1 == n2:#ou usamos "else:"
    print('Os dois valores são \033[35mIGUAIS\033[m')
