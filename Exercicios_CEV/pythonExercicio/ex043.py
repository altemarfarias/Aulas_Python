peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2) # peso dividido por altura ao quadrado
print('O IMC dessa pessoa está é {:.1f} '.format(imc))
# Classificação do IMC
if imc <= 18.5:
    print('Peso baixo')
elif imc > 18.5 and imc < 25.0:
    print('Peso normal')
elif imc >= 25.0 and imc < 30.0:
    print('Sobrepeso')
elif imc >= 30.0 and imc < 35.0:
    print('Obesidade Grau I')
elif imc >= 35.0 and imc < 40.0:
    print('Obesidade Grau II')
else:
    print('Obsidade Grau III')

