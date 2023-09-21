#! /usr/bin/env python3
'''
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar,
desconsidere-o.
'''


soma = 0
listPares = []


for c in range (1,7):
    numero = int(input(f'Digite o {c}° número: '))
    if numero % 2 == 0:
        pares = numero
        listPares.append(numero)
        soma += pares

print(f'A soma dos números pares {listPares} é {soma}')
