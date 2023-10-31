#! /usr/bin/env python3

'''
Faça um programa que leia o nome peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
a) Quantas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
'''     #0Nome #1Peso #2Nome mais leve #3 Peso mais leve #4Nome mais pesado #5 maior peso
pessoas = [[], [], [], [], [], []]

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas[0].append(nome)
    pessoas[1].append(peso)
    if len(pessoas[1]) > 0:
        pessoas[3] = max(pessoas[1])
        pessoas[5] = min(pessoas[1])

    if peso <= 70:
        pessoas[2].append(nome)
        #pessoas[3].append(peso)
    if peso >= 100:
        pessoas[4].append(nome)
        #pessoas[5].append(peso) 

    resp = input('Quer cadastrar mais pessoas? [s/n] ')

    while resp != 's' and resp != 'n':
        print('ERRO: Resposta inválida. Digite "s" ou "n"')
        resp = input('Quer cadastrar mais pessoas? [s/n] ')

    if resp == 'n':
        break

print(f'O número de pessoas cadastradas foi: {len(pessoas[0])}')
print(f'\nO maior peso foi: {pessoas[3]}Kg')

if len(pessoas[4]) > 0:
    print(f'Pessoas com 100Kg ou mais: {pessoas[4]}')
else:
    print('\nNão há pessoas com 100Kg ou mais')
    
if len(pessoas[2]) > 0:
    print(f'\nPessoas com 70Kg ou menos: {pessoas[2]}')
else:
    print('\nNão há pessoas com 70Kg ou menos')

if max(pessoas[1]) == min(pessoas[1]):
    print(f'O menor peso também foi: {pessoas[5]}Kg')

else:
    print(f'O menor peso foi: {pessoas[5]}Kg')

