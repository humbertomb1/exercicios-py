#!/usr/bin/env python3

''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
'''
print('\033[;30;42m#\033[m'*40)
print('\033[;30;42m#\033[mCONDIÇÃO DA EXISTÊNCIA DE UM TRIÂNGULO\033[;30;42m#\033[m')
print('\033[42;30m#\033[m'*40)
print('\n'*2)
reta1 = float(input('Digite o primeiro seguimento de reta: '))
reta2 = float(input('Digite o segundo seguimento de reta: '))
reta3 = float(input('Digite o terceiro segundo de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 +reta3 and reta3 < reta1 + reta2:
	print('Esses segmentos podem formar um triângulo')
else:
	print('Esses segmentos \033[31mnão\033[m podem formar um \033[32mtriângulo\033[m')
