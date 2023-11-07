#! usr/bin/env python3
'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um diconário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo.
c) Uma lista com toda as mulheres
d) Uma lista com todas as pessoas com idade acima da média do grupo

'''
database = []
ficha = {}
soma = 0
while True:
    
    ficha['nome'] = nome = str(input('Digite o nome: '))
    ficha['idade'] = idade = int(input('Digite a idade: '))
    soma += ficha['idade']
    ficha['sexo'] = sexo = str(input('Digite o sexo: [m/f]: '))
    
    database.append(ficha.copy())
    ficha.clear()
    resp = str(input('Cadastrar mais pessoas?[s/n] '))
    if resp in 'Nn':
        break


media = soma / len(database)

print()
print(f'Pessoas cadastradas: {len(database)}')
print(f"A média do grupo é: {media:.1f}")
print('=-'*20)
print()
print('Lista com toda as mulheres:', end="")
print()
for m in database:
    if m['sexo'] == 'f':
        print(f"{m['nome']}")

print('=-'*20)

print('Lista com pessoas acima da média: ')

for id in database:
    if id['idade'] >= media:
        print(f"{id['nome']}, {id['idade']} anos.")