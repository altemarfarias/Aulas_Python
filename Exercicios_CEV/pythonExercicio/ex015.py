km = int(input('Quantos Km você percoreu? '))
dias = int(input('Quantos dias ficou com o carro? '))
print('O você percoreu {}km a R$ 0.15(cada) e ficou {} dia(s) \n'
      'a R$ 60,00(cada) o valor a pagar do aluguel é R$ {:.2f}'
      .format(km, dias, (km*0.15) + (dias*60.00)))
