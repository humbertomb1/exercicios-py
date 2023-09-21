#!/usr/bin/env python3

'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num = input('Digite três números para verficarmos quem é o maior entre eles: ')


if num[0] > num[1] and num[0] > num[2]:
	print(f'Entre {num[0]}, {num[1]} e {num[2]} o maior é {num[0]}')
else:
	if num[1] > num[0] and num[1] > num[2]:
	    print(f'Entre o número {num[0]}, {num[1]} e {num[2]} o maior é {num[1]}')
	else:
		if num[2] > num[0] and num[2] > num[1]:
		   print(f'Entre o número {num[0]}, {num[1]} e {num[2]} o maior é {num[2]}')
		else:
			if num[0] and num[1] and num[2] == num[0] or num[1] or num[2]:
				print('Há dois números iguais um menor que os dois')

			
