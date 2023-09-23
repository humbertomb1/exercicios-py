#! /usr/bin/env python3
'''
Crie um programa que leia dois valores e mostre o menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

from os import system

opcao = None

while opcao != 5:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    
    opcao = int(input('''
  OPÇÕES \n
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do Programa\n
Escolha uma opção acima:
'''))
    
    #Valida se o número escolhido está entre as opções
    if opcao <= 0 or opcao > 5:
        system('clear')
        print('Opção inválida. Digite dois valores novamente:')
        continue

    if opcao == 1:
        #soma valores
        result = valor1 + valor2
        system('clear')
        print(f'A soma entre {valor1} e {valor2} é {result}\n')

    elif opcao == 2:
        #multiplica valores
        result = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {result}\n')

    elif opcao == 3:
        #Verifica um valor é maior que o outro ou iguais
        if valor1 > valor2:
            result = valor1
            system('clear')
            print(f'{valor1} é maior que {valor2}\n')

        elif valor2 > valor1:
            result = valor2
            system('clear')
            print(f'{valor2} é maior que {valor1}\n')
        else:
            system('clear')
            print(f'{valor1} é igual a {valor2}\n')

    #Volta para escolha de valores
    elif opcao == 4:
        system('clear')
        continue
    
    #Sai do programa
    elif opcao == 5:
        break

    #Sair ou não do programa depois de escolher uma opção
    voltar_sair = input('Deseja voltar para o menu de opções? [s/n]').lower()
    system('clear')

    #Laço para caso de esolha difente de 's' ou 'n'
    while voltar_sair != 'n' and voltar_sair != 's':
        voltar_sair = input('Escolha inválida. Digite "s" voltar para o menu de opções ou "n" para sair do programa: ')
        system('clear')

    if voltar_sair == 's':
        opcao = None
    else:
       break


system('clear')
print('Programa encerrado pelo usuário')