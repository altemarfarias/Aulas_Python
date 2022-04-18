#Desenvolver um programa que leia o comprimento de três retas
#e diga ao usuário de elas podem ser ou não um triângulo
r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))
podeser = False
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    podeser = True
print('As três retas pode formar um triângulo' if podeser == True else
      'As três retas NÃO pode ser um triangulo')
