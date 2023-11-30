#! usr/bin/env python3
'''
Crie um programa que tenha a função leiaint(), que vai funcionar
semelhante à função input() do Python, só que fazendo a validação
para aceitar apenas um valor númerico.
'''


def leia_int(num):

    while not num.isnumeric():
        print('Você não digitou números. Tente novamente:')
        num = input('Digite um número: ')

    return print('Você digitou um número.')


leia_int(input('Digite um número: '))
