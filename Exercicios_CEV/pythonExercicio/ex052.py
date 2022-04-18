print('Vamos ver se o numero que vai digitar é primo.')
# um numero primo só pode ser divido por 1 ou por ele
num = int(input('Digite um numero: '))
primo = False
for x in range(2, num):
    if (num % x) == 0:
        print('\033[33m', end='')
        primo = True
    else:
        print('\033[31m', end='')
    print('{}'.format(x), end=' - ')
if primo:
    print('O numero {}, que digitou  é Primo'.format(num))
else:
    print('O numere {}, que digitou NÃO é primo'.format(num))

