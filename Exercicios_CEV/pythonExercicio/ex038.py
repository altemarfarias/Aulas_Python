# Escrever um programa para destinguir se dois numeros são diferentes
num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))
if num1 > num2:
    print('O 1º = {} numero é maior que o 2º = {}'.format(num1, num2))
elif num1 < num2:
    print('O 1º = {} numero é menor que o 2º = {}'.format(num1, num2))
else:
    print('Os dois numero digitados são iguais')

