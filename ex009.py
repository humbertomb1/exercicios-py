""" 
Faça um programa que leia a largua e a altura de uma parede em metros.
Calculue sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta 2m²
"""

print('Calculando quantidade de tinta a ser gasta em litros')
altura = float(input('Quantos metros de altura? '))
compri = float(input('Quantos metros de largura? '))
metroq = altura * compri
litro = 0.5
quanti = metroq * litro
print(f'Para pintar {metroq}m² é necessário {quanti} litro(s) de tinta')
