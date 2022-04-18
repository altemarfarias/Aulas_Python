from  datetime import date
atual = date.today().year

totalmaior = 0
totalmenor = 0
for pess in range(1, 8):  # 7 pessoas
    nasci = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - nasci
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Existe {} pessoa(s) de maior'.format(totalmaior))
print('Existe {} pessoa(s) de menor'.format(totalmenor))
