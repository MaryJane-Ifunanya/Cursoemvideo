print('''Escreva um programa que leia um valor em metros e o exiba convertido
em centimetros e milimetros.''')

n1 = float(input('Uma distância em metros:'))
cm = n1 * 100
mm = n1 * 1000
dm = n1 * 10
dam = n1 / 10
hm = n1 / 100
km = n1 / 1000
print('A medida de {}m corresponde a \033[32m{:.0f}cm\033[m e \033[32m{:.0f}mm\033[m.'.format(n1, cm, mm))
print('A medida de {}m corresponde a \033[32m{:.0f}dm\033[m, \033[32m{:.0f}dam\033[m , \033[32m{:.0f}hm\033[m , e \033[32m{:.0f}km\033[m.'.format(n1, dm, dam, hm, km))

