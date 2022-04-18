print('Digite dois numeros, em seguida defina do que vai fazer conforme menu:')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
print('[1] = somar\n[2] = multiplicar\n[3] = maior\n[4] = novos numeros\n[5] = Sair do programa')
opcao = 0
while opcao != 5:
    opcao = int(input('Digite sua opçao: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, (n1 + n2)))
    if opcao == 2:
        print('A multiplicação de {} * {} = {}'.format(n1, n2, (n1 * n2)))
    if opcao == 3:
        if n1 > n2:
            print('Os numeros digitados {} e {}, o maior é {}'.format(n1, n2, n1))
        else:
            print('Os numeros digitados {} e {}, o maior é {}'.format(n1, n2, n2))
    if opcao == 4:
        print('Digite novos numros: ')
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
print('Sistema encerrado!')