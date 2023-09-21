#!/usr/bin/env python3
''' Faça um programa que leia um número de 0 a 9999
	e mostre na tela cada um dos digitos 
	separados em unidade, dezena, centena e milhar
'''
numero = int(input('Digite um número entre 0 e 9999 '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')