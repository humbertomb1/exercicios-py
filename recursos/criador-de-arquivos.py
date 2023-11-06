#! /usr/bin/env python3
'''
Programa para criar vários arquivos do tipo python
'''
import os

pasta = os.chdir("/media/humberto/midia4/TI/python/exercicios-py/")

arquivos = []

for arquivo in sorted(os.listdir(pasta)):
    if arquivo.startswith('ex') and arquivo.endswith('.py'):
        arquivos.append(arquivo)


quanti = int(input('Quantos arquivos você quer criar? '))

total = len(arquivos)



for c in range (0, quanti):
    if total < 99:
        with open(f'ex0{total +1}.py', 'x') as file:
            shebang = "#! usr/bin/env python3\n"
            l1 = "'''"
            l2 = "\n"
            l3 = "\n"
            l4 = "'''"
            file.writelines([shebang,l1,l2,l3,l4])
    else:
        with open(f'ex{total +1}.py', 'x') as file:
            shebang = "#! usr/bin/env python3"
            l1 = "'''"
            l2 = "\n"
            l3 = "\n"
            l4 = "'''"
            file.writelines([shebang,l1,l2,l3,l4])
    total += 1