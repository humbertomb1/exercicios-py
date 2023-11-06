#! usr/bin/env python3

'''
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe maior, os dois são iguais

'''

print('Digite dois números para saber qual é o maior entre eles')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'O primeiro número é maior: {numero1}')
elif numero2 > numero1:
    print(f'O segundo número é maior: {numero2}')
else:
    print('Não existe valor maior, os dois são iguais')
