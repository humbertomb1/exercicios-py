#! usr/bin/env python3

'''
Refaça o desafio dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados são iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados são diferentes
'''

seg1 = float(input('Digite o primeiro seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))


if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('- É possível formar um triângulo com esses seguimentos')
    if seg1 == seg2 == seg3: # Todos os lados iguais
        print('- É um triângulo equilátero pois todos os lados são iguais')
    if seg1 == seg2 or seg2 == seg3 or seg1 == seg3:# Ao menos dois lados são iguais
        print('- É uum triangulo Isóeceles, pois dois seguimentos são iguais')
    if seg1 != seg2 != seg3 != seg1: # Todos os lados são diferentes
        print('- É um triângulo escaleno, pois todos os lados são diferentes')
else:
    print('Não é possível formar um triângulo com esses seguimentos')
