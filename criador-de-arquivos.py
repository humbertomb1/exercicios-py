#! /usr/bin/env python3
'''
Programa para criar vários arquivos
'''
from pathlib import Path
import os

pasta = os.chdir("/media/humberto/midia4/TI/python/exercicios-py/")

arquivos = []

for arquivo in os.listdir():
    if arquivo.startswith('ex') and arquivo.endswith('py'):
        arquivos.append(arquivo)

for i, arquivo in enumerate(sorted(arquivos)):
    arquiv = Path(arquivo)
    
    if i + 1 <= 9:
        novo = f'ex00{i+ 1}{arquiv.suffix}'
    else:
        novo = f'ex0{i+ 1}{arquiv.suffix}'
    arquiv.rename(novo)

for c in sorted(arquivos):
    print(c)