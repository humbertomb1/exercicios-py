#! /usr/bin/env python3
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA '))
termos = n1 + razao
print(f'Os 10 primeiros termos dessa PA são: \033[1;33m{n1} {termos}\033[m', end=" ")

for c in range (1, 8 + 1):
    termos += razao
    print(f'\033[1;33m{termos}\033[m', end=" ")