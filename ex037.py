#! usr/bin/env python3

'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O Programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.Calcule o valor da prestação mensal, 
sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

'''

valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anosPagar = float(input('Em quantos anos você quer pagar? '))

totalmes = anosPagar*12

prestaçao = valorCasa/totalmes

salario30 = (salario/100) * 30

if prestaçao > salario30:
    print(f'A prestação mensal ultrapassa 30% do seu salário, seu emprestimo foi \033[1;31mNEGADO.\033[m')
    print(f'30% de {salario}: \033[1;31m{str(salario30).replace(".", ",")}\033[m ')
    print(f'Valor da prestação mensal: {prestaçao:.2f}')
else:
    print('Seu emprestimo foi \033[1;32mAPROVADO\033[m')
    print(f'30% de {salario}: \033[1;32m{str(salario30).replace(".", ".")}\033[m ')
    print(f'Valor da prestação mensal: {prestaçao:.2f}')