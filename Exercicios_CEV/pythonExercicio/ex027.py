nome = str(input('Digite seu nome: ')).strip()
print('O primenro nome é: ' + nome.split()[0])
posicao = len(nome.split())
print('O ultimo nome é: {}'.format(nome.split()[posicao-1]))