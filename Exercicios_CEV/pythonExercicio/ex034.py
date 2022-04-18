sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    sal = sal * 1.10
else:
    sal = sal * 1.15
print('O salário com o ajuste vai ficar R$ {:.2f}'.format(sal))





