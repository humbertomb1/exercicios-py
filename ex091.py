#! usr/bin/env python3
'''
Faça um programa que leia o nome e media de um aluno,
guardando também a situação em um dicionário.
No final, mostre o contéudo da estrutura na tela
'''
aluno = {}

nome = str(input('Digite o nome do aluno: '))
aluno['nome'] = nome
media = float(input('Digite a média do aluno: '))
aluno['media'] = media

if media < 6:
    aluno['situaçao'] = 'REPROVADO'
else:
    aluno['situaçao'] = 'APROVADO'

print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'E a situação é igual a {aluno["situaçao"]}')