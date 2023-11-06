#! /usr/bin/env python3
'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando o no final
quantos palpites foram necessários para vencer.
'''

import random
from os import system

numeros = range(1, 11)

tentativa = 0
escolha_pc = random.choice(numeros)
guess = None

print('Acabei de pensar em um núemro de 0 a 10... Tente adivinhar!')

while guess != escolha_pc: 
	
	escolha_pc = random.choice(numeros)

	
	guess = int(input('Digite seu palpite: '))

	if guess == escolha_pc:

		tentativa += 1
		system('clear')
		print(f'Você acertou! O número que pensei também foi {escolha_pc}!\nVocê precisou de {tentativa} palpites para acertar')
		
	else:
		system('clear')
		print(f'Você errou! o número que pensei foi {escolha_pc}')
		tentativa += 1 
		