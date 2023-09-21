#!/usr/bin/env python3
''' 
	Crie um programa que leia o nome de uma cidade
	e diga se ela começa ou não com o nome "SANTO"
'''

cidade = input('Nome da cidade: ').strip()

lista = cidade.split()


primeNom = lista[0].lower()

if primeNom == "santo":
	print('Essa cidade começa com o nome SANTO')
else:
	print('Essa cidade não começa com o nome SANTO')