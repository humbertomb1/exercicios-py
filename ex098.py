#! usr/bin/env python3
'''
Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como
paramêtro e mostre a mensagem com o tamanho adaptável
ex:
--------------
  Olá, Mundo!
--------------
'''


def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


texto = input('Digite um texto: ')

escreva(texto)
