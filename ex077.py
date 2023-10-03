#! /usr/bin/env python3
'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem exetenso, de zero até 20
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo po extenso
input : Digite um número entre 0 e 20:
'''

tupla = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito','Nove', 'Dez')

num = int(input('Digite um número: '))

print(tupla[num -1])