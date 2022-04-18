from datetime import date
# Faça um programa para verificar a situação de alistamento no exercito
#anoNasc = int(input('Digite o ano de nascimento do cidadão: '))
anoAtual = date.today().year
anoNasc = int(input('Digite o Ano que você nasceu: '))
idade = anoAtual - anoNasc
if idade < 18:
    tempo = 18 - idade
    print('Você só vai se alistar em {}'.format(date.today().year+tempo))
elif idade == 18:
    print('Corra e vá se alistar, esse é o seu Ano.')
else:
    tempo = idade - 18
    print('Passou do tempo de você se alistar, que era em {}'
          .format(date.today().year-tempo))

