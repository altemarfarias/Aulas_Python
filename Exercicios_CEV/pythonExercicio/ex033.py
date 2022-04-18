print('Digite três numeros e informe qua o mior e o menor')
lista = []
qnum = int(input('Digite a quantidade de numeros para comparar maior e menor: '))
for i in range(qnum):
    lista.append(int(input('Digite o {}  numero: '.format(i+1))))
print(lista)
maior = lista[0]
menor = lista[0]
for i in range(qnum-1):
    if maior < lista[i+1]:
        maior = lista[i+1]
#    print(maior)
    if menor > lista[i+1]:
        menor = lista[i+1]
#    print(menor)
print('O numero maior é {}'.format(maior))
print('O numero menor é {}'.format(menor))





