#Digite a quantos kilometros por hora você estava dirigindo
#Se ultrapassar 80km/h a multa vai custar R$ 7.00 por cada km excedido
km = float(input('Digite a velocidade do carro: '))
if km > 80.0:
    multa = (km -  80.0) * 7.00
    print('Velocidade acima do permitido, sua multa é de R${:.2f}'.format(multa))
else:
    print('Velocidade permitida')
