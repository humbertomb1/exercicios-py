#! /usr/bin/env python3
'''
Programa para criar vários arquivos
'''
import os

os.chdir("/home/humberto/Documentos/pasta-teste/")

arquivos = sorted(os.listdir())
contador = 1
verificador = []

for i, arquivo in enumerate(arquivos):
    if arquivo.endswith('py'):
        if i < 9:
            os.rename(arquivo, f'ex00{i+1}.py')
        else:
            os.rename(arquivo, f'ex0{i+1}.py')
        print(arquivo)
print(len(arquivos))
