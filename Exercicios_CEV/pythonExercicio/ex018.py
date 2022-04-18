from math import cos, sin, tan, radians
an = float(input('Digite o angulo que você deseja:'))
# Tem que antes converter o ângulo de graus para radiano
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f} '.format(an, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos(radians(an))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan(radians(an))))
