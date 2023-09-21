#! usr/bin/env python3
import requests
from bs4 import BeautifulSoup
'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 28:Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida

'''

print('CALCULANDO IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Gitei sua altura '))
imc = peso / (altura ** 2)
if imc < 17:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\nVocê está \033[1;31mmuito abaixo do peso.\033[m')
elif imc >= 17 and imc <= 18.49:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\nVocê está \033[1;33mabaixo do peso\033[m')
elif imc >=18.49 and imc <=24.99:
    print(f'\n\033[1;36mIMC\033[m: {imc:.1f}.\nVocê está com o \033[1;32mpeso ideal\033[m')
elif imc >= 24.99 and imc <= 29.99:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\nVocẽ está \033[1;33macima do peso\033[m')
elif imc >= 29.99 and imc <= 35.99:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\n 033[1;33mObesidade Grau 1\033[m')
elif imc >= 35.99 and imc <= 39.99:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\n\033[1;31mObesidade grau 2\033[m')
else:
    print(f'\033[1;36mIMC\033[m: {imc:.1f}.\n\033[1;31mObesidade Grau 3\033[m')
