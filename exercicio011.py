print('''Faça um programa que leia a alrgua e a altura de uma parede em metros,
calcule e sua área e a quantidade de tinta necessário para pinta-lá, sabendo que cada
litro de tinta, pinta uma área de 2m².''')

larg = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = larg * altura
print('Sua parede tem a dimensão de {}x{} e sua area de \033[35m{}m²\033[m.'.format(larg, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de \033[35m{}l\033[m de tinta.'.format(tinta))
