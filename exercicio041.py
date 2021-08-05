print('''A confederação Nacional de Natação precisa de um programa
 que leia o ano de nascimento de um atleta e mostra sua categoria, de acordo com a idade: 
 - Até 9 anos:\033[34mMIRIM\033[m
 - Até 14 anos:\033[34mINFANTIL\033[m
 - Até 19 anos:\033[34mJUNIOR\033[m
 - Até 25 anos:\033[34mSENIOR\03[m
 - Acima:\033[34mMASTER\033[m''')

from datetime import date
ano = int(input('Ano de Nascimento:'))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[34mMIRIM\033[m')
elif idade <=14:
    print('Classificação: \033[34mINFANTIL\033[m')
elif  idade <= 19:
    print('Classificação: \033[34mJUNIOR\033[m')
elif idade <= 24:
    print('Classificação: \033[34mSÊNIOR\033[m')
else:
    print('Classificação: \033[34mMASTER\033[m')
