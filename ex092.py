#! usr/bin/env python3
'''
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado 
'''
from time import sleep
from random import randint
from operator import itemgetter

jogadores = {
            'jogador 1': randint(1, 6),
            'jogador 2': randint(1, 6),
            'jogador 3': randint(1, 6),
            'jogador 4': randint(1, 6)
}
ranking = dict()

print('=-'*15)
print(f'{"---==SORTEIO==---":^29}')
print('=-'*15)
print()

for k, v in jogadores.items():
    print(f'   O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print()
print('=-'*15)
print(f'{"---==RAKING==---":^29}')
print('=-'*15)
print()
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)