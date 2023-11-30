#! usr/bin/env python3
'''
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
quantos gols ele marcou. O programa deverá conseguir
mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(nome, gols):
    if nome == '':
        nome = 'Desconhecido'
    elif gols == '':
        gols = 0

    return nome, gols


jogador = str(input('Nome do Jogador: '))
marcados = str(input('Gols marcados: '))

nome_jogador, gols_marcados = ficha(jogador, marcados)

print(f'O jogador {nome_jogador} fez {gols_marcados} gol(s) no campeonato')
