print('''Crie um programa que leia duas notas do aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:\033[34mREPROVADO\033[m
- Média entre 5.0 e 6.9:\033[34mRECUPERAÇÃO\033[m
- Média 7.0 ou superior:\033[34mAPROVADO\033[m''')

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é \033[32m{:.1f}\033[m'.format(n1, n2,media))
if media < 5:
    print('O aluno está \033[31mREPROVADO!\033[m')
elif 7 > media >= 5 :# ou if media >=5 and media < 7:
    print('O aluno esta em \033[36mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print('O aluno está \033[34mAPROVADO!\033[m')
