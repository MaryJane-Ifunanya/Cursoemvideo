print('''\033[34mCrie um programa que leia varios números inteiros pelo
teclado. O programa vai parar quando o usuário digitar o valor 999,
que é a condção de parada. No final mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag.\033[m''')

soma = cont = 0
while True:
    valor = int(input('Digite um valor (999 para parar):'))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')
