#!/usr/bin/env python3


''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10% 
Para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Qual é o seu salário? '))


if salario > 1250.00:
	novoSala = salario + (salario * 10) / 100
	print(f'Você tem um salário superior a R$1250,00,\nportanto sua taxa de aumento foi de 10% e seu novo salário é de R${str(novoSala).replace(".", ",")}')
else:
	salario < 1250.00
	novoSala = salario + (salario * 15 ) / 100
	print(f'Você tem um salário inferior a R$1250,00,\nportanto sua taxa de aumento foi de 15% e seu novo salário é de R${str(novoSala).replace(".", ",")}')