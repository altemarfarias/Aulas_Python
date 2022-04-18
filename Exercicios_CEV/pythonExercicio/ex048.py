print('Vamos mostrar a soma dos numeros multiplos de 3 entre 1 e 500')
soma = 0
contador =0
for cont in range(1, 501, 2):
    if (cont % 3) == 0:
        soma += cont
        contador = contador + 1
print('Existe {} numeros impares e a soma é {}'.format(contador, soma))
