#Analisador de textos
frase = 'Curso em video Python'
print(frase[9::3])
#retorno: 'vePh' = começa na coluna 10 e vai até o final de 3 em 3 colunas
print(len(frase))
#retorno: 21 = quantos caracteres tem na frase
print(frase.count('o'))
#retorn: 3 = quantos caracteres 'o' tem na frase
print(frase.count('o', 0, 13))
#retorno: 1 = quantos carracteres 'o' tem a parti da coluna 13
print(frase.find('deo'))
#retorno: 11 = a partir de qual coluna foi encontrado a parte 'deo'
print(frase.find('Android'))
#retorn: -1 = parte não encontrada na frase (-1)
print('Curso' in frase)
#retorno: True = retorna verdadeiro (True) se existe ou False caso não
print(frase.replace('Python', 'Androide'))
#retorno: 'Curso em video Androide' = substituiu a parte
#         'Python' por 'Androide'
print(frase.upper())
print(frase.lower())
#retorno: 'CURSO EM VIDEO PYTHON' = upper - transforma a frase para maiusculas
#         e o lower - para minuscula
print(frase.capitalize())
#retorno: Curso em video python = coloca só a primeira letra em maiuscula
print(frase.title())
#retorno: 'Curso Em Video Python' = coloca a letras iniciais em maiusculas
print(frase.replace('Curso', '   Cusro'))
print(frase.strip())
#retorno: elimina os espaços em branco do início e final da frase