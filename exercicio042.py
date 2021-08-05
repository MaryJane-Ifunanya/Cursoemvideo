print('''Refaça o DESAFIO 035 dos triângulo,
 acrescentando o recurso de mostrar que tipo de triângulo será formado:
  -\033[34mEquilátero:\033[m todos os lados iguais
  -\033[34mIsósceles:\033[m dois lados iguais
  -\033[34mEscaleno:\033[m todos os lados diferentes''')

n1 = float(input('Primeiro segmento:'))
n2 = float(input('Segundo segmento:'))
n3 = float(input('Terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO', end='')
    if n1 == n2 and n2 == n3:# ou n1 == n2 == n3
        print(' \033[34mEQUILÁTERO!\033[m')
    elif n1 != n2 != n3 != n1:
        print(' \033[34mESCALENO!\033[m')
    else:
        print(' \033[34mISÓSCELES!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
