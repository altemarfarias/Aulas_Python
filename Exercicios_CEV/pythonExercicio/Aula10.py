'''nome = str(input('Qual é seu nome: '))
if nome == 'Altemar':
    print('Que nome lindo!')
else:
    print('Seu nome é normal')
print('Bom dia {}'.format(nome))
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(media)
if media >= 6.0:
    print('Sua média {:.1f} está boa, PARABÉNS!'.format(media))
else:
    print('Sua média {:.1f} não está boa'.format(media))
print('PARABÉNS pela média' if media >= 6.0 else 'HUMM! estude mais' )
