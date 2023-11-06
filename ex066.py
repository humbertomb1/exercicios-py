#! /usr/bin/env python3
'''
Crie um programa que leia vários números inteiros pelo teclado.
O Programa só vai parar quando o usuário digitar 999, que é 
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (descosiderandoa flag)
'''



numero = 0
soma = 0 # criar uma variável para somar todos os números que foram digitados
total = 0 # criar variável para totalizar números digitados
while numero != 999: #criar um laço

    numero = int(input('Digite um número. (999 Para para o programa):')) #criar uma variavel para ler input do teclado dentro do laço

    if numero != 999: #criar uma condição para desconsiderar a flag
        soma += numero
        total += 1
print(f'A soma foi {soma}. O total de números digitados foi {total}')