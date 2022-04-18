cid = str(input('Digite o nome de sua cidade: ')).strip()
#.strip no final elimina os espaós em branco no inicio e no final
#Verificar se no nome da cidade tem a palavra  SANT
if 'SANTO' in cid.upper().split()[0]:
    simounao = ''
else:
    simounao = 'NÃO'
print('Sua cidade {} começa com a palavra SANTO'.format(simounao))
