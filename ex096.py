#! usr/bin/env python3
'''
Aprimore o desafio 94 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
'''

database = []
data = dict()
gols = []

while True:

    data['nome'] = nome = str(input('Nome do jogador '))

    part = int(input(f'Quantas partidas {data["nome"]} jogou? '))

    for g in range(0, part):
        gol = int(input(f'Quantos gols na partida? {g + 1} '))
        gols.append(gol)
        
    data['gols'] = gols.copy()
    data['total'] = sum(gols)
    database.append(data.copy())

    gols.clear()
    data.clear()
    
    resp = str(input('Quer continuar? [s/n]'))
    if resp in 'Nn':
        break

print('=-='*20)
print('cod', end=" ")

for i in database:
    for k, c in  i.items():
        print(f"{k:<13}", end="")

print()
print('-'*28)


for k, item in enumerate(database):
    print(f"{k:<3}", end=" ")
    for c ,v in item.items():
        print(f"{str(v):<5}", end=" ")

print()
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    print(len(database) -1)
    if cod > len(database) -1:
        print('Código invalido!')
        continue
    elif cod == 999:
        break
    print(f'Levantamento do jogador {database[cod]["nome"]}')
    print()
    
    for i, c in enumerate(database[cod]['gols']):
        print(f'No jogo {i +1} ele fez {c} gols ')
    print()