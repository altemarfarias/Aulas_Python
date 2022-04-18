# CONVERSÃO PARA BINÁRIO, OCTAL OU HEXADECIMAL
numero = int(input('Digite um numero inteiro: '))
print('Escolha a opção a qual pretende converter:\n'
      '1 = binário\n'
      '2 = octal\n'
      '3 = hexadecimal')
opcao = int(input('Digite o numero da opção desejada: '))
if opcao == 1:
    print('O numero em binário é: {}'.format(bin(numero)))
elif opcao == 2:
    print('O numero em octal é: {}'.format(oct(numero)))
else:
    print('O numero em hexadecial é {}'.format(hex(numero)))

