#! /usr/bin/env python3
'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos
'''
peso_lista = []


print('-=-' *9)
print(' LENDO MAIOR E MENOR PESO')
print('-=-' *9, "\n")




for c in range(1 , 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    peso_lista.append(peso)    

maior_peso = max(peso_lista)
menor_peso = min(peso_lista)
print(f'Maior Peso: {maior_peso}Kg\nMenor Peso: {menor_peso}Kg')



# USANDO TECNICA DE REGISTRAR O MENOR PESO ANTES DO LOOP

#registrando a menor peso antes do loop
#menor_peso = peso

#for c in range(2, 6):
#    peso = float(input(f'Digite o peso da {c} pessoa: '))
#    if peso > maior_peso:
#        maior_peso = peso
        
#    elif peso < menor_peso:
#        menor_peso = peso
