#! /usr/bin/env python3
'''
Faça um programa que soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500
'''
soma = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
print(f'A soma entre todos os ímpares múltimos de 3 entre 1 e 500 é {soma}')