#! /usr/bin/env python3
'''
Crie um program que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando espaços.
ex: APOS A SOPA
A SACA DA CASA
A TORRE DA DERROTA
'''

frase = input('Digite uma frase para verificarmos se ela é ou não um palíndromo: ')


frase = "".join(frase.split()).lower()
lista = []
cont = len(frase)


for c in frase:
    #Adiciona a cadeia de caractéries de trás para frente
    lista.append(frase[cont -1])
    cont += - 1


lista = "".join(lista)

# Testa se 'lista e 'frase' são iguais
if lista == frase:
    print('É um palíndromo')
else:
    print('Não é palíndromo')