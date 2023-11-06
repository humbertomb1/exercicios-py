#! /usr/bin/env python3

''' 
Crie um programa que vai ler vários e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados
b) A lista de valores, ordenada e forma crescente
c) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    resp = input('Quer digitar mais números? [s/n]')
    
    while resp != 's' and resp != 'n':
        print('ERRO: Você não escolheu uma opção válida')
        resp = input('Quer digitar mais números? [s/n]')
    
    if resp == 'n':
        break
print(f'Foram digitados {len(valores)} números')
print(f'Lista ordenada: {sorted(valores)}')

if 5 not in valores:
    print('O valor 5 não está na lista')
else:
    print('O valor 5 está na lista')