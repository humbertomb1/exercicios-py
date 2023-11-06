#! /usr/bin/env python3
'''
Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifícios
indo de 10 até 0, com uma pausa de 1 segundo entre eles
'''
from time import sleep
lista = ['UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE','DEEEEZ']
cont = 0
for c in range(10, 0, -1):
    print(lista[0 + cont])    
    sleep(1)
    cont += 1
print('PA... PA PA APAPAPAPAPPAPAPA BOOOOM!!')