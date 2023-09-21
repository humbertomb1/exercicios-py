#! /usr/bin/env python3

numero = int(input('Digite um número: '))

print('''
===================
TABELA DE CONVERSÃO
[1] Para binário
[2] Para octal
[3] Para hexadecimal
''')

escolha = int(input('Digite no número :'))

if escolha == 1:
    binario = bin(numero)
    print(f'O número{numero} convertido para binário é {binario}')
elif escolha == 2:
    octal = oct(numero)
    print(f'O número {numero} convertido para octal é {octal}')
elif escolha == 3:
    hexaD= hex(numero)
    print(f'O Número {numero} convertido para hexadecimal é {hexaD}')
else:
    print('OPÇÃO INVÁLIDA')