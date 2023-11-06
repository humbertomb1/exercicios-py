#! usr/bin/env python3

'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acorde com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de ele se alistar
- Se já passou do tempo de alistamento
Mostrar também o tempo que falta ou que passou do prazo

'''

print('STATUS DE ALISTAMENTO')
nasci = int(input('Digite o seu ano de nascimento: '))
anoAtual = 2023
idade = anoAtual - nasci

if idade == 18:
    print('Você tem 18 anos ou completa esse ano, está na hora de se alistar')
elif idade < 18:
    falta = 18 - idade # Calcula o tempo que ainda falta para o alistamento
    print(f'Você tem menos de 18 anos, ainda falta {falta} ano(s) para você se alistar')
elif idade > 18:
    passou = idade - 18 # Calcula o tempo que já passou
    print(f'Você já passou dos 18 e já passou {passou} ano(s) do prazo de alistamento')
