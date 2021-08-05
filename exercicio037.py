print('''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário que será a \033[34mbase de conversão\033[m:
-\033[34m1\033[m para \033[35mbinário\033[m
-\033[34m2\033[m para \033[35moctal\033[m
-\033[34m3\033[m para \033[35mhexadecimal\033[m''')

num = int(input('Digite um numero inteiro:'))
print('''Escolhe uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção invalida. Tente novamente.\033[m')
