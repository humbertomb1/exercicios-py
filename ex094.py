#! /usr/bin/env python3

'''
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um bletim
contendoa média de cada um e permita que o usuário possa mostrar
notas de cada aluno individualmente
'''
from os import system
database = []


while True:

    data = [[]]

    aluno = input('Nome: ')
    data.insert(0, aluno)
    nota1 = float(input('Nota 1: '))
    data[1].append(nota1)

    nota2 = float(input('Nota 2: '))
    data[1].append(nota2)

    database.append(data.copy())

    media = sum(data[1]) / len(data[1])

    data[1].append(media)
    
    data.clear()

    resp = input('Quer continauar? [s/n]? ')
    while resp != 's' and resp != 'n':
        resp = input("ERRO: Você não digitou nem 's' nem 'n'. Tente novamente: ")
    if resp == 'n':
        break

system('clear')
print('No.\tNOME\tMÉDIA')
print('-'*20)


for i, c in enumerate(range(0, len(database))):
    print(f"""{i} \t{database[i][0]} \t {database[i][1][2]}""")
 
    
while True:
   
    chave = int(input('\nMostrar nota de qual aluno? (999 interrompe): '))
    
    if chave == 999:
        break

    print(f'Notas de {database[chave][0]}:', end="")
    
    for c in range(0, 2):
        
        print(f' {database[chave][1][c]}', end=" ")



#[['Fernanda', [7.0, 8.0, 7.5]], ['Maria', [9.0, 8.0, 8.5]]]