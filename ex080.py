#! /usr/bin/env python3

'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os primeiros pares
'''

tupla = (int(input('Digite um número ')), int(input('Digite um número ')), int(input('Digite um número ')), int(input('Digite um número ')))

cont9 = 0

for nove in tupla:
    if nove == 9:
     cont9 += 1

print(f'\nVezes que o número nove apareceu: {cont9}\n')

if 3 in tupla:
    print(f'O número três foi encontrado na posição {tupla.index(3)}')
else:
    print('O número 3 não foi digitado\n')


print('\nOs pares foram:', end=" ")
for par in tupla:
    if par % 2 == 0:
        print(par, end=" ")
print('\n')

