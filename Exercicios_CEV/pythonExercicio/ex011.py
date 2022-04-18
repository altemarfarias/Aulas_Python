print('Vamos calcular a quantidade de tinta '
      'precisa para pintar uma parede.')
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede:'))
print(('Sua parede tem {:.2f} x {:.2f} e tem {:.2f}m2'.format(altura,largura, altura*largura)))
print('É necessário {:.3f} litros de tinta para pintar'
      .format((altura*largura)/2))
