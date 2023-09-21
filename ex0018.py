# Sorteando um item numa lista
from random import choice
aluno1 = input('Primeiro aluno ')
aluno2 = input('Segundo aluno ')
aluno3 = input('Terceiro aluno ')

lista = [aluno1, aluno2, aluno3]
escolha = choice(lista)
print(f'o aluno sorteado foi {escolha}')