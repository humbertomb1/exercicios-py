#!/usr/bin/env python3
#Sorteando uma ordem na lista
from random import shuffle
aluno1 = input('Primeiro aluno ')
aluno2 = input('Segundo aluno ')
aluno3 = input('Terceio aluno ')
aluno4 = input('Quarto aluno ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem sorteada foi')
print(lista)