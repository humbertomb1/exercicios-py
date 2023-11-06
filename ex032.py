#!/usr/bin/env python3

''' Faça um programa em que leia o ano qualquer e mostre se ele é bissexto'''

ano = str(input('Digite um ano para verificarmos se ele é bissexto: '))
doisprim = int(ano[:2]) # Os dois primeiros números
doisult = int(ano[2:]) # Os dois últimos números


if doisult % 4 == 0 and doisult != 00: # Testa se os dois ultimos números são divisíveis por 4 e não são iguais a 00
	print('Ano bissexto')
else:
	if doisprim % 4 == 0 and doisult == 00: # Verdadeiro se o resto da divisão por 4 de 'doisprim' é igual a 0 e os dois últimos números são iguais a 00
		print('Ano bissexto')
	else:
		print('Não é ano bissexto')

