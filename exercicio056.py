print('''Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa , mostre:
[ 1 ] A média de idade do grupo.
[ 2 ] Qual é o nome do homem mais velho
[ 3 ] Quantas mulheres têm menos de 20 anos.''')
somaidade = 0
mediaidade = 0
maioridade_homem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade_homem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
