#!/usr/bin/env python3
#Crie um programa que leia o nome completo de uma pessoa
# E mostre: 
# Nome com todas as letras minúsculas
# Nome com todas as letras maúsculas
# Quantas letras tem(sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Dgite nome e sobrenome: ')

maius = nome.upper() # Com letras maiúsculas

minus = nome.lower() # Com letras minúsculas

separador = nome.split() # Lista com nomes separados

juntador = "".join(separador) # String com nome juntado

primCont  = len(separador[0]) # Contador de caracteres do primeiro nome

contLetra = len(juntador) # Contador de caracteres


print(f'Com letras maiúsculas: {maius}')
print(f'Com letras minúsculas:`{minus}')
print(f'Total de letras sem contar espaços: {contLetra}')
print(f'Total de letras no primeiro nome: {primCont}')