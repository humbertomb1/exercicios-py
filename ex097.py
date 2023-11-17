#! usr/bin/env python3
'''
Faça um programa que tenha a função
chamda area(), que receba as dimensões
de um terreno retangular (largura e comprumento) e
mostre a àrea do terreno
'''

print('Controle de Terrenos')
print('-'*20)


def area(larg, compri):
    resul = larg * compri
    return print(f'A área de um terreno de {larg} x {compri} é de {resul}m²')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
