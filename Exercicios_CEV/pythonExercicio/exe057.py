sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    print('Sexo Inválido')
    sexo = str(input('Digite novamente o sexo (M ou F): ')).upper()
if sexo == 'M':
    print('A pessoa tem o sexo Masculino')
else:
    print('A pessoa tem o sexo Feminino')
