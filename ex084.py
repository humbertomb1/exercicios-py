#! /usr/bin/env python3

'''
Crie um programa onde o usuário possa digitar vários valores númericos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados
em ordem crescente.
'''
lista = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor)
    
    
    escolha = input('Quer adicionar mais números? [s/n] ').lower()

    while escolha != 's' and escolha != 'n':

        print('ERRO: Você não digitou "s" nem "n"')
        escolha = input('Quer adicionar mais números? [s/n] ').lower()
        
    if escolha == 'n':
        break
    else:
        continue
    
print(f'Os valores digitados em ordem crescente: {sorted(lista)}')