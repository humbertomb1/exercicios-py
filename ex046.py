#! usr/bin/env python3

'''
Elabore um programa que calcule o valor a ser pago por um produto, considere o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

'''

valor = float(input('Preço das compras: R$'))

print("====FORMAS DE PAGAMENTO====")
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] Em até 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    novoValor = valor - (valor*10/100)
    print(f'Sua compra de R${valor} vai custar R${novoValor} no final.')
elif opcao == 2:
    novoValor = valor - (valor*5/100)
    print(f'Sua compra de R${valor} vai custar R${novoValor} no final')
elif opcao == 3:
     parcela = valor / 2
     print(f'Sua compra de R${valor} será divida em 2x no cartão e com parcelas de {parcela} vai custar R${valor} no final.')
elif opcao == 4:
    parcela = int(input('Em quantas vezes? '))
    novoValor = valor + (valor*20/100)
    valorParc = novoValor / parcela
    print(f'Sua compra ficou no total de {novoValor} parcelado em {parcela}x de {valorParc}')
    