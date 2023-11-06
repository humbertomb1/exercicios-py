#! /usr/bin/env python3
'''
Faça um programa que leia um número inteiro e diga se ele é ou não um primo
OBS: se o número for 7 o método range tem que ser de 1 a 7
'''
numero = int(input('Digite um número para sabermos se ele é primo ou não '))
total = 0

for c in range(1, numero + 1):
    # Testa se o resto da divisão é zero
    if numero % c == 0:
        total += 1 # contador de resto de divisões

# Testa se o total do resto das divisões que foram contadas é igual a 2
if total == 2:
    print('\033[1;32mÉ Primo\033[m')
else:
    print('\033[1;31mNão é primo\033[m')