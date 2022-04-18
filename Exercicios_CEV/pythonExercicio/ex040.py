nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Média {:.1f} é abaixo de 5.0 = REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Média {:.1f} está entre 5.0 e 6.9 = RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Media {:.1f} maior ou igual a 7.00 = APROVADO'.format(media))
else:
    print('Deve ter havido um erro de digitação')