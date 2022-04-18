from time import sleep
from random import randint
print('A maquina pensou em um numero, tente advinhar qual esse numero')
nMaquina = randint(1, 10)
nUsuario = int(input('Digite uma numero dentre 1 a 10: '))
sleep(1)
vezes = 1
while nMaquina != nUsuario:
    nUsuario = int(input('Você não acertou, digite outro numero entre 1 a 10:'))
    vezes += 1
print('Você fez {} tentativa(s), o numero que a máquina pensou foi {}'.format(vezes, nMaquina))
