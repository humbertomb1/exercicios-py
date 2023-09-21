#!/usr/bin/env python3
import random

'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 0 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu'''


lista = [0, 1, 2, 3, 4, 5]
numCerto = random.choice(lista)
print('Vou pensar em um número de 0 5... Tente adivinhá-lo, ok?')
escolha = int(input('Vamos lá, escolha um número: '))
	
if escolha == numCerto:
	print(f'Você acertou! O número que eu pensei foi {numCerto}')
else:
	print(f'Você errou! O número que eu pensei foi {numCerto}')

