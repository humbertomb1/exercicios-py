#! /usr/bin/env python3

'''
Faça um program que leia um número qualquer e mostre o seu
fatorial.
ex:
5! = 5x4x3x2x1= 120
'''
fatorando = int(input('Digite um número '))

cont = fatorando
fator = 1
print(f'Calculando {fatorando}! = ', end="")
while cont > 0:
    print(f'{cont} x ' if cont > 1 else f'{cont} = ', end="")
    fator *= cont
    cont -= 1
print(fator)