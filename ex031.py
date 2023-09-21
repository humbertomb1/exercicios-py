#!/usr/bin/env python3


''' 'Desenvolva um programa que pergunte a distância de uma viagem em Km.
  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 0,45 para viagens mais longas.
'''

distancia = float(input('Qual foi a distância percorrida? '))
taxa200 = distancia * 0.50
taxa = distancia * 0.45

if distancia <= 200.0:
  print(f'Você percorreu {distancia}Km. Sua taxa por Km rodado foi de R$0,50 e o total a pagar é R${taxa200}')
else:
  print(f'Você percorreu {distancia}Km. Sua taxa por Km rodado foi de R$0,45 e o total a pagar é R${taxa}')
