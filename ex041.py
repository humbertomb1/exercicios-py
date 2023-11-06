#! usr/bin/env python3
from datetime import date
'''
Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até: 19 anos: JUNIOR
- até 20 anos; SÊNIOR
- acima: MASTER
'''
print('CLASSIFICANDO CATEGORIA POR IDADE')
data1 = date.today()
data2 = int(data1.strftime("%Y"))

nasci = int(input('Em que ano você nasceu? '))
idade = data2 - nasci

if idade <= 9:
    print('ATLETA MIRIM')
elif idade >= 10 and idade <= 14:
    print('ATLETA INFANTIL')
elif idade >= 15 and idade <=19:
    print('ATLETA JUNIOR')
elif idade == 20:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')