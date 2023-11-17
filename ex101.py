#! usr/bin/env python3

'''
Faça um programa que tenha uma lista
chamada números e duas funções
chamdas sorteia() e somaPar().
A primeira lista vai sortear 5 números
e vai colocá-los numa lista e a
segunda função vai mostrar a soma entre todos os
valores PARES sorteados pela função anterior
'''
from random import randint


def sorteia(a, b):
    numeros = [randint(a, b), randint(a, b), randint(a, b), randint(a, b), randint(a, b)]
    return numeros


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    return soma


print(soma_par(sorteia(1, 5)))
