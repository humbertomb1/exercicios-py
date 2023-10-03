#! /usr/bin/env python3
'''
Crie um programa que vai gerar cinco números aleatórios e vai
colocar em uma tupla
Depois disso, mostre a listagem de números gerados
e também o menor e o maior valor que estão na tupla
# Talvez criar cinco tuplas e depois contatenálos em uma tupla?
'''
import random


tupla = (random.sample(range(5), 5))
print('Sequência: ', end="")
for c in tupla:
    print(c, end=" ")

print(f'\n\nMenor valor: {min(tupla)}')
print(f'\nMaior valor: {max(tupla)}')