#! usr/bin/env python3
'''
Faça um mini-sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM' o programa se encerrará. Usar cores.
'''


def cabeca():
    print('~'*28)
    print('  SISTEMA DE AJUDA PYHELP')
    print('~'*28)


while True:
    cabeca()
    print('Função ou Biblioteca')
    resp = input('>').lower()
    if resp == 'fim':
        break
    else:
        help(f"{resp}")





