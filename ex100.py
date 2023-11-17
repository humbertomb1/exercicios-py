#! usr/bin/env python3
'''
Faça um programa que tenha uma função
chamada maior(), que receba vários
paramêtros com valores inteiros.
Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
'''

def maior(*num):
    print(max(num))


maior(2, 4, 6, 8, 9)