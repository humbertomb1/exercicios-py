#!/usr/bin/env python3

'''Escreva um programa que leia a velocdade de um carro. 

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

veloci = float(input('Em que velocidade estava o carro? '))

if veloci > 80.0:
	acimaLimit = veloci - 80.0
	calcLimit = 7.0 * acimaLimit
	print(f'O veículo estava acima do limite de 80Km/h e foi multado em R${calcLimit}')
else:
	print(f'O veículo estava no limite de 80Km/h e não foi multado.')
