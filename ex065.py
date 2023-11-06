#! /usr/bin/env python3
'''
Escreva um programa que leia um número n inteiro
e mostre na tela os n primeiros elementos de uma sequência
de fibonacci.
'''
print('='*22)
print('SEQUÊNCIA DE FIBONACCI')
print('='*22)
termos = int(input('\nQuantos termos você quer mostrar? '))

cont = 3
n1 = 0
n2 = 1

print(n1, n2, end=" ")

while cont <= termos:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
    cont += 1
