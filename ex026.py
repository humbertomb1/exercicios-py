#!/usr/bin/env python3
''' 
	Faça um programa que leia o nome de uma pessoa,
	mostrando em seguinda o primeiro e o último nome dela separadamente
'''
n = str(input('Digite seu nome Completo: \n')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')

