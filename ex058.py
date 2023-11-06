'''
Convertendo decimal para binário com loop
'''
from os import system

decimal = int(input('Digite o decimal: '))
dividendo = decimal
lista_resto = []

for c in range(dividendo):
    resto = dividendo % 2
    lista_resto.append(resto)
    quoci = dividendo // 2 # pegando o quociente da divisão
    dividendo = quoci # quociente passa a ser o dividendo
    if dividendo == 0: # Parar o loop uma vez que dividendo chegue a 0
        break

system('clear')

# invertendo a ordem da lista
lista_resto.reverse()
str_bin = "".join(str(bit) for bit in lista_resto)

print(f'\033[1;32m{decimal}\033[m em binário é \033[1;33m{str_bin}\033[m')
