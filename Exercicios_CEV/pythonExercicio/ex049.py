n = int(input('Digite um numero de 1 a 9, que mostraremos a tabuada: '))
print('=' * 12)
for cont in range(1, 10):
    print('{} x {} = {}'.format(n, cont, n*cont))
print('*' * 12)
