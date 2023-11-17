#! usr/bin/env python3
'''
Faça um programa que tenha a função
chamda area(), que receba as dimensões
de um terreno retangular (largura e comprumento) e
mostre a àrea do terreno
'''

print('Controle de Terrenos')
print('-'*20)

def area(largura, compri, area):
    print(f'A área de um terreno de {largura} x {compri} é de {area}m²')

largura = float(input('LARGURA (m): '))
compri = float(input('COMPRIMENTO (m): '))
resul = largura * compri

area(largura, compri, resul)