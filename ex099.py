#! usr/bin/env python3
'''
Faça um programa que tenha ua função contador(),
que receba três paramêtros: início, fim, e passo
e realze a contagem.
Seu programa tem que realizar três contagens através da função craida:

a) De 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada. 
O usuário que vai definir o inicío, fim e passo
'''

from time import sleep


def barra():
    sleep(1)
    print('-='*20)


def contador(inicio, fim, passo):

    contagem = inicio
    print('Contagem de 1 até 10 de 1 em 1:')
    print()
    while contagem <= fim:
        print(contagem, end=" ")
        sleep(0.5)
        contagem += passo
        

    print('\n')
    barra()
    inicio = 10
    fim = 0
    passo = 2
    contagem = inicio
   
    print('Contagem de 10 até 1 de 2 em 2:')
    print()
    while contagem >= fim:
        sleep(0.5)
        print(contagem, end=" ")
        contagem -= passo
    
    print('\n')
    barra()
    print('Agora é Sua vez de personalizar a contagem!')
    print()
   
    inicio = int(input('Inicio: '))
    fim = int(input('fim: '))
    passo = int(input('Passo: '))
    contagem = inicio

    if inicio < fim:
        if passo == 0:
            passo = 1
        while contagem <= fim:
            sleep(0.5)
            print(contagem, end=" ")
            contagem += passo
    elif inicio > fim:
        if passo < 0:
            passo = abs(passo)
        elif passo == 0:
            passo = 1
        contagem = inicio
        while contagem >= fim:
            print(contagem, end=" ")
            sleep(0.5)
            contagem -= passo


contador(1, 10,1)
