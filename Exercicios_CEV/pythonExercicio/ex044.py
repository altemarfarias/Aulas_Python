print('{:=^40}'.format('ACF DESIGNER'))
# {:=^40} = centralizado em 40 espaços
preco = float(input('Preço das compras: R$ '))
print('''FORMA DE PAGAMENTO:
[ 1 ] - Dinheiro
[ 2 ] - A vista Cartão
[ 3 ] - 2x no Cartão
[ 4 ] - 3x ou Mais no Cartão
''')
# Opção 1 = (-)10%; 2 = (-)5%; 3 = 0%; 4 = (+)20%
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    print('Valor da compra R$ {:.2f} e o valor a pagar R$ {:.2f}'
          .format(preco, preco*0.9))
elif opcao == 2:
    print('Valor da compra R$ {:.2f} e valor a pagar: R$ {:.2f}'
          .format(preco, preco*0.95))
elif opcao == 3:
    print('Valor da compra R$ {:.2f} e valor a pagar: R$ {:.2f}'
          .format(preco, preco))
elif opcao == 4:
    quantParc = int(input('Quantas parcelas: '))
    print('Valor da compra R$ {:.2f} e valor a pagar: R$ {:.2f}'
          .format(preco, preco*1.2))
    print('Sua compra vai ser dividida em {} de R$ {:.2f}'
          .format(quantParc, (preco*1.2)/quantParc))
else:
    print('Opção Inválida!')


