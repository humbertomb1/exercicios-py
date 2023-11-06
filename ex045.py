#! /usr/bin/env python3

'''
Crie um programa que faça o computador jogar Jokenpô com você

'''
from random import choice
from time import sleep

print('Suas opções:')
print('[ 0 ] \033[1;31mPEDRA\033[m')
print('[ 1 ] \033[1;32mPAPEL\033[m')
print('[ 2 ] \033[1;33mTESOURA\033[m')
print('='*15,'\n')
jogada = int(input('Qual é a sua jogada? '))
print('\n')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaPC  = choice(lista)
print('Pronto?! Vamos lá.\n')
sleep(1)
print('...\n')
sleep(1)
print('PEDRA\n')
sleep(1)
print('PAPEL\n')
sleep(1)
print('TESOUUUURAA!\n')
sleep(1)

if jogada == 0:
    if escolhaPC == 'PEDRA':
        print(f'EMPATE!\nTambém escolhi \033[1;31m{escolhaPC}\033[m!')
    if escolhaPC == 'PAPEL':
        print(f'GANHEI!\nEscolhi\033[1;32m{escolhaPC}\033[m! E \033[1;32mPAPEL\033[m Vence \033[1;31mPEDRA\033[m!')
    if escolhaPC == 'TESOURA':
        print(f'VOCÊ GANHOU!\nEscolhi \033[1;33m{escolhaPC}\033[m! E \033[1;31mPEDRA\033[m vence \033[1;33mTESOURA\033[m!')
elif jogada == 1:
    if escolhaPC == 'PAPEL':
            print(f'EMPATE!\n Também escolhi \033[1;32m{escolhaPC}\033[m!' )
    if escolhaPC == 'PEDRA':
            print(f'VOCÊ GANHOU!\n Escolhi \033[1;31m{escolhaPC}\033[m! E \033[1;32mPAPEL\033[m vence \033[1;31mPEDRA\033[m!')
    if escolhaPC == 'TESOURA':
            print(f'GANHEI!\n Escolhi \033[1;33m{escolhaPC}\033[m! E\033[1;33m{escolhaPC}\033[m vence \033[1;32mPAPEL\033[m!')
elif jogada == 2:
    if escolhaPC == 'TESOURA':
        print(f'EMPATE!\nTambém escolhi \033[1;33m{escolhaPC}\033[m!')
    if escolhaPC == 'PEDRA':
        print(f'GANHEI!\nEscolhi \033[1;31m{escolhaPC}\033[m! E \033[1;31m{escolhaPC}\033[m vence \033[1;33mTESOURA\033[m!')
    if escolhaPC == 'PAPEL':
        print(f'VOCê GANHOU!\nEscolhi \033[1;32m{escolhaPC}\033[m! E \033[1;33mTESOURA\033[m vence \033[1;32m{escolhaPC}\033[m!')
else:
     print('JOGADA INVÁLIDA! Você não escolheu nenuma das opções acima')