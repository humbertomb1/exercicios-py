#! /usr/bin/env python3

'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a 
expressão passada está com os parênteses abertos
e fechados na ordem correta

'''

expressao = [input('Digite uma expressão: ')]
aberto = 0
fechado = 0

for parent in expressao:
    for contaPar in parent:
        if '(' in contaPar:
            aberto += 1
        elif ')' in contaPar:
            fechado += 1

if fechado != aberto:
    print('Expressão inválida')
else:
    print('Expresão válida')