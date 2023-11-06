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

    aluno = input('Nome: ')
    
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    database.append([aluno, [nota1, nota2], media])

    resp = input('Quer continauar? [s/n]? ')
    
    while resp != 's' and resp != 'n':
        resp = input("ERRO: Você não digitou nem 's' nem 'n'. Tente novamente: ")
    
    if resp in 'n':
        break

system('clear')
print(f'{"No.":<4} {"NOME":<10} {"MEDIA":>8}')
print('-'*25)

for i, c in enumerate(range(0, len(database))):
    print(f"""{i:<4} {database[i][0]:<8}  {database[i][2]:>8}""")
 
while True:
   
    chave = int(input('\nMostrar nota de qual aluno? (999 interrompe): '))
    
    if chave == 999:
        break
    
    print('=-'*15)

    if chave <= len(database) -1:
        print(f'\nNotas de {database[chave][0]}: {database[chave][1]}')
    else:
        print('Aluno inválido.')
    


#[['Fernanda', [7.0, 8.0, 7.5]], ['Maria', [9.0, 8.0, 8.5]]]