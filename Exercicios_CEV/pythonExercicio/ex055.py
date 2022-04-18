# Vamos digitar o peso de 5 pessoas, ver o que tem o peso maior e o que tem o peso menor
pesomaior = 0
pesomenor = 0
for x in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        pesomenor = peso
        pesomaior = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O peso MAIOR é {}'.format(pesomaior))
print('O peso MENOR é {}'.format(pesomenor))


