#! usr/bin/env python3

'''
Crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média atingita:
- Média abaixo de 5.0: REPROVADO
- Média entre 6.0 e 6.9: RECUPERAÇÃO
- Média de 7.0 ou superior: APROVADO

'''
print('TIRANDO MÉDIA DE DUAS NOTAS')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 5.0 or media <= 6.0:
    print(f'\033[1;31mREPROVADO\033[m: Média de {media}')
elif media > 6.0 and media <= 6.99:
    print(f'\033[1;33mRECUPERAÇÃO\033[m: média de {media}')
elif media >= 7:
    print(f'\033[1;32mAPROVADO\033[m: média de {media}')

