#! /usr/bin/env python3
'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
'''
from datetime import date

data = date.today()
ano_atual = int(data.strftime("%Y"))

total_menor = 0
total_maior = 0


for c in range(1, 8):
    nasci = int(input(f'Digite o ano de nascimento da {c} pessoa: '))
    idade = ano_atual - nasci
    if idade < 18:
        total_menor += 1
    else:
        total_maior += 1


print(f'{total_menor} pessoas não atigiram a maior idade\ne {total_maior} já são maiores de idade')