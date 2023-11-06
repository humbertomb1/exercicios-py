#! /usr/bin/env python3

''' 
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

a) Qual é o total gasto na compra
b) Quantos produtos custam mais de 1000.
c) Qual e o nome do produto mais barato
'''
import locale

cont = mais_mil = total = mais_barato = 0

while True:
    print('#'*30)
    print('     SIMULADOR DE CAIXA')
    print('#'*30, '\n')

    nome = input('Qual o nome do produto? ')
    preço = float(input('Qual é o preço do produto ?'))
    total += preço
     # checa primeira iteração e pega produto mais barato
    if cont == 0:
        mais_barato = preço
        nome_barato = nome
    cont += 1
    #Verifica se 'preço' é menor que 'mais_barato' e adiciona nome a 'nome_barato'
    if preço < mais_barato: 
        nome_barato = nome
        mais_barato = preço
    #Verifca se preço é maior que mil e adiciona mais 1 a 'mais_barato
    if preço > 1000: 
        mais_mil += 1
    
    resp = input('Quer continuar? [S/N]').lower().strip()

    while resp != 's' and resp != 'n':
        resp = input('Quer continuar? [S/N]').lower().strip()
    if resp == 'n':
        break

    
print(f'- Total de gasto na compra: R${total}')
print(f'- Quantos produtos custaram mais de mil: {mais_mil}')
print(f'- O nome do produto mais barato foi {nome_barato} e custou R${mais_barato}')