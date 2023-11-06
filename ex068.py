#! /usr/bin/env python3

''' 
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicidado
for negativo.
'''
cont = 1
while True:
    print('-==-'*10)
    print('               TABUADAS    \n')
    print('Digite -1 para encerrar o programa')
    print('-==-'*10, '\n')

    produto = int(input('Quer ver a tabuada de qual número? '))
    if produto == -1:
        break
    while cont < 10:
        produto2 = produto * cont
        print(f'{produto} x {cont} = {produto2} ')
        cont += 1
    print('~'*35, '\n')

print('Programa encerrado pelo usuário.')