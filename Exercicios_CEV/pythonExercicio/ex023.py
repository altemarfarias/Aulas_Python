num = str(input('Digite um número entre 0 a 9999: '))
num = num.zfill(4)
print('unidade: {} dezena: {} centena: {} milhar: {}'
      .format(num[3:4], num[2:3], num[1:2], num[0:1]))
print(num)
#OUTRA MANEIIRA DE RESOLVER
numero = int(input('Digite um numero entre 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('A unidade é {}:'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('A milhar é: {}'.format(m))