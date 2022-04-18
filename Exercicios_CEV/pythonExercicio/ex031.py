dist = float(input('Digite a distancia da viagem a percorrer: '))
print('O valor da passaigem a ser paga é R${:.2f}'.format(dist*0.50)
      if dist <= 200.00 else
      'O valor da passaigem a ser paga é R${:.2f}'.format(dist*0.45))
