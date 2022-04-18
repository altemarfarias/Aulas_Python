r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª rata: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos acima pode formar um TRIANGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos NÃO pode formar uma TRIANGUL0')