# Digitar uma frase e dizer se é um PALINDROMO
frase = input('Digite uma frase: ').upper()
palavras = frase.split()
juntos = ''.join(palavras)
invertida = ''
for x in range(len(juntos) - 1, -1, -1):
    invertida = invertida + juntos[x]

print('Você digitou a frase: {}'.format(frase))
print('Palavras separadas: {}'.format(palavras))
print('Palavras juntas: {}'.format(juntos))
print('Palavras invertidas: {}'.format(invertida))

if juntos == invertida:
    print('Essa frase é um PALINDROMO')
else:
    print('Essa frase NÃO é um PALINDROMO')
