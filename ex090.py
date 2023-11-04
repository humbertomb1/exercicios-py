#! /usr/bin/env python3

'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadstre-os em uma list única que mantenha separados pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
valores = [[], []]

for cont in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

if len(valores[0]) > 0:
    print(f'\nPares: {sorted(valores[0])}')
else:
    print('\nNão há valores pares nessa sequência')

if len(valores[1]) > 0:
    print(f'\nÍmpares: {sorted(valores[1])}')
else:
    print('\nNão há valores ímpares nessa sequência')