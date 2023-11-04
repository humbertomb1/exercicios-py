#! /usr/bin/env python3

'''
Crie um programa que crie uma matriz de dimensão 3x3
Preencha com valores lidos pelo teclado, no final mostre a matriz
na tela com a formatação correta
'''

matriz = [[],[],[]]

for cont in range(1, 10):

    if cont <= 3:
        num = int(input(f'Digite um número para 0, {len(matriz[0])}: '))
        matriz[0].append(num)
    elif cont <= 6:
        num = int(input(f'Digite um número para 1, {len(matriz[1])}: '))
        matriz[1].append(num)
    elif cont <= 9:
        num = int(input(f'Digite um número para 2, {len(matriz[2])}: '))
        matriz[2].append(num)

for i, c in enumerate(matriz[0]):
    print(f'[{c}]', end=" ")
    if i == 2:
        print('\n')

for i, c in enumerate(matriz[1]):
    print(f'[{c}]', end=" ")
    if i == 2:
        print('\n')
    


for c in (matriz[2]):
    print(f'[{c}]', end=" ")
    
