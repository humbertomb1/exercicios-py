#! /usr/bin/env python3
'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 termos da progreesão usando a estrutura while
'''
print('MOSTARANDO OS 10 PRIMEIROS TERMOS DE UMA PA\n')
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o razão '))
termo = n1
cont = 1
print('Os 10 primeros termos: ', end="")
while cont <= 10:
    termo += r
    cont += 1
    print(termo, end=" ")