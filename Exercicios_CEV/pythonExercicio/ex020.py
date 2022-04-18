from random import shuffle
print('Digite o nome dos 4 alunos a ser sorteados: ')
listAlunos = []
for x in range(4):
   listAlunos.append(input('Digite o {}º aluno: '.format(x+1)))
input('Agora vamos ao sorteio: (Enter)')
shuffle(listAlunos)
for x in range(4):
   print('O {}º do sorteio é : {}'.format(x+1, listAlunos[x]))

