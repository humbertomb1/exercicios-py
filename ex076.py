#! /usr/bin/env python3

while True:
    print('~='*20)
    print('             BANCO IQQ')
    print('          Caixa eletronico')       
    print('~='*20, '\n')
    print('Esse caixa só opera com notas de 50, 20, 10 e 1 real\n')

    cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0

    saque = int(input('\nDigite o valor do saque: R$'))

    print('*' *30)
    while saque >= 50:
        cedula_50 +=  1
        saque -=  50

    if cedula_50 > 0:
        print(f'Total de {cedula_50} de cédulas de R$50\n')

    while saque >= 20:
        cedula_20 += 1
        saque -= 20

    if cedula_20 > 0:
        print(f'Total de {cedula_20} de cédulas de R$20\n')
    

    while saque >= 10:
        cedula_10 += 1
        saque -= 10

    if cedula_10 > 0:
        print(f'Total de {cedula_10} de cédulas de R$10\n')
   
    while saque >= 1:
        cedula_1 += 1
        saque -= 1

    if cedula_1 > 0:
        print(f'Total de {cedula_1} de cédulas de R$1\n')
    print('*' *30, '\n')

    resp = input('Quer sacar mais? [sim/não] ').lower().strip()

    while resp != 'sim' and resp != 'não':
        resp = input('Quer sacar mais? [sim/não] \n').lower().strip()

    if resp == 'não':
            break
print('\nO BANCO IQQ agrace a sua preferência. Volte sempre!\n')