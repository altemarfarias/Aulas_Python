nome = str(input('Digite seu nome: '))
if nome == 'Altemar':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Jose':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))
