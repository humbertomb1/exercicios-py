#! /usr/bin/env python3

'''
Crie um programa que leia vários números e colocar em uma list.
Depois disso, crie duas listras extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente
Ao final, mostre o conteúdo das três listas geradas.
'''
valores = []
impar = []
par = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)

    resp = input('Quer digitar mais números? ')
    
    while resp != 's' and resp != 'n':
        print('ERRO: Você digitou uma opção errada')
        resp = input('Quer digitar mais números? ')
    if resp == 'n':
        break

for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Lista de números digitados: {valores}')

if len(par) > 0:
    print(f'Valores pares: {par}')

else:
    print('Não há valores pares')

if len(impar) > 0:
    print(f'Valores impares: {impar}')
    
else:
    print('Não há valores impares')