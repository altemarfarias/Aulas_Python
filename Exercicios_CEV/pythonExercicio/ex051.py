print('Vamos fazer uma programa que mostre o primeiro'
      'termo e a razao de um PA')
pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
dt = pt + (11 - 1) * rz
cont = 0
for x in range(pt, dt, rz):
    cont = cont + 1
    print('O {}º termo é: {}'.format(cont, x))

