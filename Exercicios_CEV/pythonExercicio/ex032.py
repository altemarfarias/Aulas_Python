from datetime import date
from calendar import isleap
ano = int(input('Digite o ano: '))
print('{} é um ano BISSEXTO'.format(ano)
      if isleap(ano) else
      '{} NÃO é um ano BISEXTO'.format(ano))
#Vamos usar o 0 para definir a data atual
if ano == 0:
      ano = date.today().year
#Outra forma de fazer
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      print('O ano de {} é BISSEXTO'.format(ano))
else:
      print('O ano de {} não é BISSEXTO'.format(ano))
