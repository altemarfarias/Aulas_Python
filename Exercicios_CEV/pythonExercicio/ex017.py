#Como calcular a hipotenusa de um triangulo
'''catO = float(input('Qual o comprimento do cateto Oposto: '))
catA = float(input('Qual o comprimento do dateto adjacente: '))
HipT = (catO ** 2 + catA ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(HipT))'''
from math import hypot
catO = float(input('Digite o cateto oposto: '))
catA = float(input('Digite o cateto adjacente: '))
hipT = hypot(catO, catA)
print('A hipotenusa é {:.2f}'.format(hipT))
