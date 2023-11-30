#! usr/bin/env python3
'''
Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo fatorial.

'''
from time import sleep
from math import factorial as fac


def fatorial(num, show=False):
    if show:
        print('Calculando fatorial...')
        for f in range(1, num):
            sleep(0.5)
            num *= f
            print(num, end=" ")
    else:
        print(f'Fatorial de {num}')
        print(fac(num))


fatorial(5, show=True)
