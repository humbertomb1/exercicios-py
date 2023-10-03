#! /usr/bin/env python3
'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços,
na sequencia.
No final, mostre uma listagem de preços, organizados os dados em forma tabular
'''

tupla = iter(('Lapis', 2.50, 'Borracha', 3.00, 'Caderno', 15.00, 'Mochila', 50.00,))
 
for items in tupla:
    preço = next(tupla)
    print(f'{items}.............: {preço:.2f}')