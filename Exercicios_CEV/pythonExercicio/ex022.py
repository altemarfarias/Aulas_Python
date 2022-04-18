nome = str(input('Digite seu nome completo:')).strip()
#.strip no final elimina os espaós em branco no inicio e no final
#Listar nome com letras aiusculas
print(nome.upper())
#listar nome do letras menusculas
print(nome.lower())
#Quantidade de letras existente no nome
print(len(nome))
#Quantidade de letras exisrtente se contar os espaços
print(len(''.join(nome.split())))
print(len(nome) - nome.count(' '))
#Quantidade de letras da primeira palavra
print(len(nome.split()[0]))
