#! /usr/bin/env python3
'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da excecução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores
'''
from os import system

lista = []
cont = 's'
menor = maior = media = soma = total = 0

while cont == 's':

    numero = int(input('Digite os números:'))
    total += 1
    soma += numero

    if total == 1: # receber o menor valor na primeira iteração
        menor = numero
    else:
        if numero > maior: # checa se 'número' é maior que 'maior'
            maior = numero
        if numero < menor: #checa se 'número' é menor que 'menor'
            menor = numero

    cont = input('Quer continuar? [s/n]').lower()

media = soma / total # Tirando a média

system('clear')

print(f'''
- A média foi {media:.2f}
- O maior número foi {maior}
- O menor número foi {menor} 
- Você digitou {total} números
''')