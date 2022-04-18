print('Vamos calcular o ajuste de salário de 15%')
sal = float(input('Digite o salário atual:'))
print('O salário com o ajuste fica R$ {:.2f} e passou a ganhar '
      'R$ {:.2f}'.format((sal*15/100), sal + (sal*15/100)))
