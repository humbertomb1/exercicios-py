#! /usr/bin/env python3
'''
Refaça o desafio 009 mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for
'''
produto = int(input('Tabuada de que número você quer ver? '))
print(F'''
=-=-=-=-=-=-=-=-=-
  TABUADA DE {produto}
=-=-=-=-=-=-=-=-=-
''')
for p in range(1, 11):
    result = produto * p
    print(f'\033[1;32m{produto}\033[mx{p} = {result}') 