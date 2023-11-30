#! usr/bin/env python3
'''
Crie uma função que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.
'''


def voto(nasc):
    from datetime import date
    data = date.today()
    ano = int(data.strftime('%Y'))
    idade = ano - nasc

    if idade < 16:
        return f'NEGADO \nIdade: {idade} anos'
    elif idade <= 17:
        return f'OPCIONAL \nIdade: {idade} anos'
    elif 18 <= idade < 65:
        return f'OBRIGATÓRIO \nIdade: {idade} anos'
    elif idade > 65:
        return f'OPCIONAL \nIdade: {idade}anos'


nascimento = int(input('Digite o ano de nascimento: '))


print(f'{voto(nascimento)}')
