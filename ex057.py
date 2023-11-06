#! /usr/bin/env python3
# Quando uma função que foi criada pelo usuário é chamada, no final dela aparece 'none'
# Até aqui não estudei funções para entender o porquê

'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo
- Qual é o homem mais velho
- Quantas têm menos de 20 anos
'''
from os import system

def cabecalho():
    print('-=-' *10)
    print('       REGISTRANDO GRUPO')
    print('-=-' *10)

mais_velho = 0
menor_20 = 0
mais_velho = 0
nome_velho = ''
lista_idade = []


for c in range(1, 5):
    print(cabecalho())
    nome = input(f'Digite o nome da {c} pessoa: ').lower().strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').lower()
    lista_idade.append(idade)
    system('clear')
    if sexo == 'homem':
        #Se sexo for homem verficiar se idade é maior que mais velho e coletar nome
        if idade > mais_velho:
            mais_velho = idade
            nome_velho = nome
    # Testa se 'idade' tem menos de 20 e adiciona mais um a variável 'menor_20'       
    if idade < 20:
        menor_20 += 1 

    # Calcula a média de idade do grupo
media = sum(lista_idade) / len(lista_idade) 

def tem_homem():

    print(f'''
        - A média de idade do grupo foi {media:.2f}
        - O homem mais velho é {nome_velho.capitalize()} e ele tem {mais_velho} anos
        - {menor_20} pessoa(s) tem menos de 20 anos
    ''')

def sem_homem():
        print(f'''
        - A média de idade do grupo foi {media:.2f}
        - Não há homens no grupo
        - {menor_20} pessoa(s) tem menos de 20 anos
    ''')
        
if nome_velho == '' and mais_velho == 0:
     print(cabecalho())
     print(sem_homem())
else:
     print(cabecalho())
     print(tem_homem())
