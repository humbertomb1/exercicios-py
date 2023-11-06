#! /usr/bin/env python3

'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto
''' 
sexo = input('Digite o sexo da pessoa [F/M]:').upper()

while sexo != 'M' and sexo != 'F':
   print(f'Você não digitou "F" ou "M". Tente novamente. Letra digitada: {sexo}')
   sexo = str(input('Digite o sexo da pessoa [F/M]:')).upper()

else:
    print(f'Você digitou corretamente!')
    