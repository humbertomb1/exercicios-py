#! /usr/bin/env python3

''' 
Crie um programa onde o usuário possa digitar cinco valores
númericos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar sort).
No final, mostre a lista ordenada na tela
'''
valores = []
cont = 0
while cont < 5:
    num = int(input('Digite um número: '))
    valores.append(num)
    if len(valores) >= 2:
        pass