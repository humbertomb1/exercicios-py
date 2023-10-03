#! /usr/bin/env python3
'''
Crie um programa que tenha uma tupla
com várias palavras(não usar acentos)
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''
'''
tupla = ('Humberto', 'Moura', 'Adriana', 'William')
ind = 0
cont = 0
while cont < len(tupla):
    print(f'\n\nAs vogais da palavra {tupla[cont].upper()} são:', end=" ")
    
    for letra in tupla[ind].lower():
           
        if letra == 'a':
                print(f'{letra}', end=" ")
        elif letra == 'e':
                print(f'{letra}', end=" ")
        elif letra == 'i':
                print(f'{letra}', end=" ")
        elif letra == 'o':
                print(f'{letra}', end=" ")
        elif letra == 'u':
                print(f'{letra}', end=" ")
    cont +=1
    ind += 1
print('\n')
'''

palavras = ('Humberto', 'Renan', 'Adriana', 'William', 'Onicia')

for palavra in palavras: #iterando sobre a lista
    print(f'\nNa palavra {palavra.upper()} temos ', end="")
    for letra in palavra: # iterando sobre cada palavra da lista
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=" ")