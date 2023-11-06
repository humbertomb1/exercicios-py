#! /usr/bin/env python3

'''
Aprimore o desfaio da matriz mostrando no fina:
a) A soma entre todos os pares digitados.
b) A soma entre valores da terceira coluna
c) O maior valor da segunda linha
'''
from os import system

matriz = [[], [], [], [], []]

for cont in range(1, 10):

    if cont <= 3:
        num = int(input(f'Digite um número para 0, {len(matriz[0])}: '))
        if num % 2 ==  0:
            matriz[3].append(num)
        if cont == 3:
            matriz[4].append(num)

        matriz[0].append(num)
    elif cont <= 6:
        num = int(input(f'Digite um número para 1, {len(matriz[1])}: '))
        if num % 2 ==  0:
            matriz[3].append(num)

        if cont == 6:
            matriz[4].append(num)

        matriz[1].append(num)
    elif cont <= 9:
        num = int(input(f'Digite um número para 2, {len(matriz[2])}: '))
        if num % 2 ==  0:
            matriz[3].append(num)

        if cont == 9:
            matriz[4].append(num)

        matriz[2].append(num)

system('clear')
print('-'*13)
print(' MATRIZ 3X3')
print('-'*13)
print(end="\n")

for i, c in enumerate(matriz[0]):
    print(f'[{c}]', end=" ")
    if i == 2:
        print(end="\n")

for i, c in enumerate(matriz[1]):
    print(f'[{c}]', end=" ")
    if i == 2:
        print(end=("\n"))
    

for c in (matriz[2]):
    print(f'[{c}]', end=" ")

print('\n')
print(f'A soma entre todos os pares digitdos foi: {sum(matriz[3])}')

print(f'\nA soma entre os valoeres da terceira linha foi: {sum(matriz[4])}')

print(f'\nO maior valor da segunda linha foi {max(matriz[1])}')
