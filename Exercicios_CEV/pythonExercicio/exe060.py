print('*' * 5, 'Calcular o fatorial de um numero:', '*' * 5)
num = int(input('Digite um numero e mostraremos seu fatorial: '))
seq = 1
tot = num
print('{}! = {}'.format(num, num), end="" )
while seq != num:
    tot = tot * (num - seq)
    print(' * {} '.format(num-seq), end="")
    seq += 1
print(' = {}'.format(tot))
