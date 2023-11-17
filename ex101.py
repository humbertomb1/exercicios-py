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


def soma_par():
    numeros = sorteia(1, 20)
    soma = 0
    for par in numeros:
        if par % 2 == 0:
            soma += par
    print(soma)


soma_par()

