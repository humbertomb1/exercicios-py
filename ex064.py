#! /usr/bin/env python3
'''
Melhore o desafio 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. o programa encerra quando ele
disser que quer mostrar zero termos
'''

n1 = int(input('Qual é o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = int(input('Quantos termos você quer mostrar dessa PA? '))

termo = n1

while cont > 0:
    print(termo, end=" ")
    termo += r 
    cont -= 1
    if cont == 0:
        cont = int(input('\nQuer mostrar mais termos? Digite 0 para encerrar o programa: '))