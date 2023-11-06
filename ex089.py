#! /usr/bin/env python3

'''
Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta
inpute inicial: "Quantos jogos vocÊ que que eu sorteie?"
'''
from time import sleep
import random
from os import system
print('=-' *20)
print('    GERADOR DE JOGOS PARA MEGA-CENA')
print('-='*20, '\n')

sorteio = int(input('Quantos jogos você quer sortear? '))
jogos = []
gerador = []
num = 0


for contador in range(0, sorteio):

    for vezes in range(0, 6):

        num = random.randint(1, 60)

        while num in gerador:
            num = random.randint(1, 60)

        gerador.append(num)
  
    jogos.append(gerador.copy())

    gerador.clear()

system('clear')
print('=-' *20)
print('    GERADOR DE JOGOS PARA MEGA-CENA')
print('-='*20, '\n')

print(f'LISTA COM {sorteio} JOGOS: ', end="\n\n")
for i, c in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {c}\n')