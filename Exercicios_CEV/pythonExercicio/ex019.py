import random
print('Vamos digitar o nome de 4 alunos e no final'
      'vamos sortear qual deles irá apagar o quadro')
nome = []
for x in range(4):
    nome.append(input('Digite o nome do {}º aluno: '.format(x+1)))
input('Pronto, dê um Enter e será sortiado')
'''alunosortiado = random.randint(0, 3)
print('O aluno sorteado foi o {}º = {}'
      .format(alunosortiado+1, nome[alunosortiado]))'''
#Outra maneira de fazer
alunosorteado = random.choice(nome)
print('O aluno sorteado foi {}'.format(alunosorteado))

