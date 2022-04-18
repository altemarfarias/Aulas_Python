n = int(input('Digite um numero inteiro:'))
print('='*10)
for x in range(9):
    print('{} x {} = {}'.format(n, x+1, n*(x+1)))
print('='*10)