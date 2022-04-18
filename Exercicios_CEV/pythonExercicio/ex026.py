frase = str(input('Digite uma frase: ')).strip()
print('Existe {} vez(es) a palavra A na frase'.format(frase.upper().count('A')))
if 'A' in frase.upper():
    print('A letra A aparece pela primeira vez na posição {}'
          .format(frase.upper().find('A')+1))
    print('A letra A aparece pela ultima vez na posição {}'
          .format(frase.upper().rfind('A')+1))
else:
    print('Na frasa não existe a letra A')