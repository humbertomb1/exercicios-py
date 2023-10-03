#! /usr/bin/env python3

''' 
Faça um programa para jogar par ou impar com o computador.
Só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consequitivas que ele conquistou no final do jogo
'''
from random import choice
from os import system

lista = ['impar', 'par']
total = soma = 0

while True:
    print('*' *30)
    print('     JOGO PAR OU IMPAR')
    print('*' *30, '\n')


    pc_impar_par = ''
    pc_num = choice(range(5))
    escolha_usr = ''
    
    while escolha_usr != 'par' and escolha_usr != 'impar': #laço para escolha apenas de 'impar e par'
        escolha_usr = input('Escolhe Par ou Impar? ').lower().strip()
        
        if escolha_usr == 'par':
            pc_impar_par = 'impar'
        else:
            pc_impar_par = 'par'
        
        system('clear')

    usr_num = int(input('Qual número vai jogar? ')) # input para escolha do jogador
    system('clear')
    while usr_num > 5:
        usr_num = int(input('Qual número vai jogar? '))
    
    soma = pc_num + usr_num # soma jogada do computador e jogador

# se pc escolhe par e usuario escolhe impar e resultado par: PC GANHA
    if pc_impar_par == 'par' and escolha_usr == 'impar' and soma % 2 == 0:
        print('~'*30)
        print('      COMPUTADOR VENCEU\n')
        print(f'Computador escolheu par e jogou {pc_num}\n')
        print(f'Jogador escolheu impar e jogou {usr_num}\n')
        print(f'Soma entre as duas jogadas: {soma}')
        print('~'*30, '\n')
        # se usuário perder encerra o programa
        break


# se pc escolhe impar e usuário escolhe par e resultado impar: PC GANHA
    if pc_impar_par == 'impar' and escolha_usr == 'par' and soma % 2 != 0:
        print('~'*30)
        print('      COMPUTADOR VENCEU\n')
        print(f'Computador escolheu impar e jogou {pc_num}\n')
        print(f'Jogador escolheu par e jogou {usr_num}\n')
        print(f'Soma entre as duas jogadas: {soma}')
        print('~'*30, '\n')
# se o usuário perder encerra o programa
        break

# se usuário esolhe par e pc escolhe impar e resultado par = USUARIO GANHA
    if escolha_usr == 'par' and pc_impar_par == 'impar' and soma % 2 == 0:
        print('~'*30)
        print('      JOGADOR VENCEU\n')
        print(f'Computador escolheu impar e jogou {pc_num}\n')
        print(f'Jogador escolheu par e jogou {usr_num}\n')
        print(f'Soma entre as duas jogadas: {soma}')
        print('~'*30, '\n')
# se o usuário ganhar soma mais um
        total += 1
# se usuário escolhe impar e pc escolhe par e resultado impar = usuario ganhar

    if escolha_usr == 'impar' and pc_impar_par == 'par' and soma % 2 != 0:
        print('~'*30)
        print('      parJOGADOR VENCEU\n')
        print(f'Computador escolheu par e jogou {pc_num}\n')
        print(f'Jogador escolheu impar e jogou {usr_num}\n')
        print(f'Soma entre as duas jogadas: {soma}')
        print('~'*30, '\n')

# se o usuário ganhar soma mais um
        total += 1
    
print(f'JOGO ENCERRADO!\n\nTotal de vitórias consecultivas do joador: {total}')