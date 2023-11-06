#! /usr/bin/env python3

''' 
Faça um programa que leia 5 valores númericos e guarde-os em uma lista
No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista
Note que se tiver valores iguais é necessário mostrar a chave dos dois valores

'''
from os import system
lista = [int(input('Digite um valor ')), int(input('Digite outro valor ')), int(input('Digite mais um valor ')), int(input('Digite o penúltimo valor ')), int(input('Digite o último valor '))]
maior = []
menor = []


for i, num in enumerate(lista):
    if num == max(lista):
        maior.append(i)
    elif num == min(lista):
        menor.append(i)

system('clear')

print(f'Você digitou os valores {lista}')


print(f'\nO maior valor foi {max(lista)} nas posições ', end="")
for i in maior:
    print(f'{i}...', end=" ")


print(f'\n\nO menor valor foi {min(lista)} nas posições ', end="")
for i in menor:
    print(f'{i}...', end=" ")
print('\n\n')