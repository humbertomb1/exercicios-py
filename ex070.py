#! /usr/bin/env python3

''' 
Crie um programa que leia a idade e a o sexo
de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer
ou não continuar, no final mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

from os import system

#Criar um loop para perguntar se usuário quer continuar
idade = menos_20 = homens = 0

while True:
    
     #iniciar viriáveis para idade e sexo
    sexo = input('Qual é o sexo da pessoa? [M/F] ').lower().strip()

    while sexo != 'masculino' and sexo != 'feminino':
        
        sexo = input('Qual é o sexo da pessoa? [M/F] ').lower().strip()

    resp_idade = int(input('\nE a idade? '))
    
    # Criar condição para pessoas que tem mais de 18 anos
    if resp_idade > 18:
        idade += 1
    # Criar condição para quantos homens foram cadastrados
    if sexo == 'masculino':
        homens += 1
    # Criar condição para quantas mulheres tem menos de 20 anos.
    if sexo == 'feminino' and resp_idade < 20:
        menos_20 += 1

    resp = input('\nQuer continuar? [S/N] ').lower().strip()
    while resp != 's' and resp != 'n':
       resp = input('\nQuer continuar? [S/N] ').lower().strip()
    system('clear')
    if resp == 'n':
        break


print(f'- Homens cadastrados: {homens}')
print(f'- Pessoas com mais de 18 anos: {idade}')
print(f'- Mulheres com menos de 20 anos: {menos_20}')