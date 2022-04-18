from random import randint
from time  import sleep
numero = randint(1, 3)
numusu = int(input('Digite um numero de 1 a 3: '))
print('PROCESSANDO...')
sleep(1)
print('Numero sorteado é {}'.format(numero))
if numero == numusu:
    print('Você venceu')
else:
    print('Você perdeu'.format(numero))
