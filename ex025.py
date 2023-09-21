#!/usr/bin/env python3
''' 
	Faça um programa que leia uma frase pelo teclado e mostre:
	- Quantas vezes aparece a letra "A"
	- Em que posição ela aparece a primeira vez
	- Em que posição ela aprece pela última vez
'''
frase = str(input('Digite uma frase:\n')).upper().strip()

contador = frase.count('A')

primPos = frase.find('A')

print(f'A letra A aparece {contador} vezes na frase')
print(f'A letra A aparece pela primeira vez no index {primPos + 1}')
print(f'A letra A aparece pela priveira vez no na posição', frase.rfind('A') + 1)
