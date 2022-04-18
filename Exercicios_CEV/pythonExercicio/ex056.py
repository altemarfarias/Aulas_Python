# Digitar um programa que leia nome, sexo e idade de 4 pessoas
# Qual a média de idade do grupo
# Quantas mulheres tem menos de 20 anos
# Qual é o nome o homem mais velho

somaidade = 0
mediaidade = 0
idademaisvelho = 0
nomemaisvelho = ''
mulhermenos20 = 0
for x in range(1, 5):
    print('-' * 15)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(x)))
    sexo = str(input('Digite o sexo (M=Mansculino e F=Feminino): ')).strip()
    idade = int(input('Digite a idade dessa pessoa: '))
    somaidade = somaidade + idade
    print('x = {}'.format(x))
    if x == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > idademaisvelho and sexo in 'Mm':  # se sexo for iqual a M ou m
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo in 'Ff':
        mulhermenos20 = mulhermenos20 + 1
somaidade = somaidade / 4
print('A média das idades é {}'.format(somaidade))
print('O homem mais velho é {}'.format(nomemaisvelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulhermenos20))




