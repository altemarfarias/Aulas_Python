from datetime import date
ano = int(input('Digite a data de Nascimento do Atleta: '))
idade = date.today().year - ano
print('A idade desse atleta é {} e sua categoria atleta é: '.format(idade))
if idade <= 9:
    print('MIRIM ')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')