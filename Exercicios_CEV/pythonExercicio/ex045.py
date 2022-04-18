from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Qual a sua jogada: 
[0] - Pedra
[1] - Papel
[2] - Tesoura
''')
jogada = int(input('Qual a sua opção? '))
print('=*' * 11)
print('O Computador jogou: {}'.format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogada]))
print('=*' * 11)
if computador == 0: # 0 = PEDRA
    if jogada == 0: # = PEDRA
        print('EMPATE')
    elif jogada == 1: # 1 = PAPEL
        print('JOGADOR VENCEU')
    elif jogada == 2: # 2 = TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
if computador == 1: # 0 = PAPEL
    if jogada == 0: # = PEDRA
        print('COMPUTADOR VENCEU')
    elif jogada == 1: # 1 = PAPEL
        print('EMPATE')
    elif jogada == 2: # 2 = TESOURA
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
if computador == 2: # 0 = TESOURA
    if jogada == 0: # = PEDRA
        print('JOGADOR VENCEU')
    elif jogada == 1: # 1 = PAPEL
        print('COMPUTADOR VENCEU')
    elif jogada == 2: # 2 = TESOURA
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')



