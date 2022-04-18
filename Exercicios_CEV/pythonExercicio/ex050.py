print('Digite 6 numenros inteiro, some apenas os pares: ')
soma = 0
for x in range(6):
    nume = int(input('Digite o {}º : '.format(x+1)))
    if nume % 2 == 0:
        soma = soma + nume
print('A soma dos numeros pares é iguaa a: {}'.format(soma))