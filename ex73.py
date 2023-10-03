#! /usr/bin/env python3
import os
pasta = os.listdir('/home/humberto/Documentos/exercicios-python/')
ord = sorted(pasta)
exerc = []
for ex in ord:
    if ex.startswith('ex') and ex.endswith('py'):
        exerc.append(ex)


cont = sorted(exerc, key=len)
conta = 1

for ex in cont:
    os.rename(ex, f'ex{conta}.py')
    conta += 1

for i, c in enumerate(cont):
    print(cont[i])
print(len(cont))