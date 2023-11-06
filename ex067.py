#! /usr/bin/env python3

''' 
Crie um programa que leia vários números inteiros pelo teclado. 
O Programa vai para quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitado e qual foi a soma entre eles (desconsiderando a flag)
'''
soma = 0
while True:
    numero = int(input('Digite um número :'))
    if numero == 999:
        break
    soma += numero
print(f'A soma foi {soma}')