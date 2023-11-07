#! usr/bin/env python3
'''
Crie um programa que gerencie o aproveitamente de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gos feito durante o campeonato
os gols tem que estar dentro de uma lista
'''
from os import system
from time import sleep
ficha = dict()
lista_gols = []
nome = str(input('Nome do Jogador: '))
ficha['nome'] = nome

partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))


for c in range(1, partidas + 1):
    gol = int(input(f'Quantos gols {ficha["nome"]} marcou na partida {c}? '))
    lista_gols.append(gol)
system('clear')
print()
ficha['gols'] = lista_gols.copy()
ficha['total'] = sum(ficha['gols'])



print(f"O jogador {ficha['nome']} jogou {partidas} partidas")


for i, p in enumerate(range (1, partidas +1)):
    print(f'  => Na partida {p}, fez {ficha["gols"][i]} gols', end="")
    print()
    sleep(1)
print()
print(f'Foi um total de {ficha["total"]} gols')

print()

print(f"O campo nome tem valor {ficha['nome']}")
print(f"O campo gols tem valor {ficha['gols']}")
print(f"O campo total tem valor {ficha['total']}")

print()
print('Dicionário completo: ')
print()
for c, v in ficha.items():
    print(f"{c}: {v}")