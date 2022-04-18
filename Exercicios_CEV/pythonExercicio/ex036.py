#SIMULADOR DE EMPRESTIMO
valorImovel = float(input('Qual o valor do Imóvel? R$ '))
salario = float(input('Qual seu salário? R$ '))
parcelas = int(input('Em quantos anos pretende pagar? '))
parcelas = parcelas*12
valorPestacao = valorImovel/parcelas
valorParcela = valorImovel/parcelas
valorMaxParc = salario*0.30
print('Quantidade de parcelas é: {}'.format(parcelas))
print('Valor da Parcela Mensal R$ {:.2f}'.format(valorParcela))
print('Parcela Maxima Permitido é R$ {:.2f}'.format(valorMaxParc))
if valorPestacao>valorMaxParc:
    print('Infelizmente seu salário não é compatível')
else:
    print('Emprestimo liberado')